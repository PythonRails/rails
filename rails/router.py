from __future__ import absolute_import
import os
import sys
import traceback
from webob.exc import HTTPNotFound, HTTPInternalServerError
from .config import Config
from .config import get_config
from .request import Request
from .response import Response
from .exceptions import PageNotFound
from .tools import import_module
from .views import View


class Router(object):
    """
    Main project router that calls appropriate controller.

    TODO:
    - decorate each controller's call with middleware
    - (done) load all controllers and their actions to dict to speedup
      lookup of desired url address
    """

    def __init__(self):
        """
        Load all controllers.

        It allow us to speed-up get controller by given url.
        """
        self._controllers = {}
        self._project_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self._load_config()
        self._load_controllers()
        self._init_view()

    def __call__(self, environ, start_response):
        """
        Find appropriate controller for requested address.

        Return Response object that support the WSGI interface.
        """
        request = Request(environ)
        try:
            controller_name = request.get_controller_name()
            action_name = request.get_action_name()
            action_handler = self.get_action_handler(controller_name, action_name)
            if not callable(action_handler):
                # action handler should be a callable function
                raise PageNotFound(
                    "Controller '{name}' doesn't have action '{action}'",
                    name=controller_name,
                    action=action_name
                )
            resp = action_handler(request)
            if not isinstance(resp, Response):
                raise Exception("Controller should return Response object, but given '{}'".format(type(resp)))
        except PageNotFound as err:
            message = self._format_error_message(str(err), with_traceback=True)
            return HTTPNotFound(message)(environ, start_response)
        except Exception as err:
            message = self._format_error_message(str(err), with_traceback=True)
            return HTTPInternalServerError(message)(environ, start_response)

        return resp(environ, start_response)

    def _load_config(self):
        """
        Load config for current project.
        """
        self._config = Config()

    def _load_controllers(self):
        """
        Load all controllers from folder 'controllers'.

        Ignore files with leading underscore (for example: controllers/_blogs.py)
        """
        for file_name in os.listdir(os.path.join(self._project_dir, 'controllers')):
            # ignore disabled controllers
            if not file_name.startswith('_'):
                module_name = file_name.split('.', 1)[0]
                module_path = "controllers.{}".format(module_name)
                module = import_module(module_path)
                # transform 'blog_articles' file name to 'BlogArticles' class
                controller_class_name = module_name.title().replace('_', '')
                controller_class = getattr(module, controller_class_name)
                controller = controller_class()
                for action_name in dir(controller):
                    action = getattr(controller, action_name)
                    if action_name.startswith('_') or not callable(action):
                        continue
                    url_path = "/".join([module_name, action_name])
                    self._controllers[url_path] = action
        return self._controllers

    def _init_view(self):
        """
        Initialize View with project settings.
        """
        views_engine = get_config('rails.views.engine', 'jinja')
        templates_dir = os.path.join(self._project_dir, "views", "templates")
        self._view = View(views_engine, templates_dir)

    def _format_error_message(self, msg, with_traceback=False):
        if with_traceback:
            tb = traceback.format_exc()
            msg += "<h3>Traceback</h3>\n\n<pre>{}</pre>".format(tb)
        return msg

    def get_action_handler(self, controller_name, action_name):
        """
        Return action of controller as callable.

        If requested controller isn't found - return 'not_found' action
        of requested controller or Index controller.
        """
        try_actions = [
            controller_name + '/' + action_name,
            controller_name + '/not_found',
            # call Index controller to catch all unhandled pages
            'index/not_found'
        ]
        # search first appropriate action handler
        for path in try_actions:
            if path in self._controllers:
                return self._controllers[path]
        return None
