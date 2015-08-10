from __future__ import absolute_import
import os
import sys
import traceback
from webob.exc import HTTPNotFound, HTTPInternalServerError
from .request import Request
from .response import Response
from .exceptions import PageNotFound
from .tools import import_module


class Router(object):
    """
    Main project router that calls appropriate controller.

    TODO:
    - load all controllers and their actions to dict to speedup
      lookup of desired url address
    - call appropriate method with get/post/put/delete prefix
    - decorate each controller's call with middleware
    """

    def __init__(self):
        """
        Load all controllers.

        It allow us to speed-up get controller by given url.
        """
        self._controllers = {}
        self._project_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self._load_controllers()

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
                # TODO: find solution for CamelCase names of controllers
                controller = getattr(module, module_name.title())
                self._controllers[module_name] = controller()
        return self._controllers

    def get_controller_by_name(self, name):
        """
        Return controller by name.
        """
        return self._controllers.get(name, None)

    def get_controller_action(self, controller, action_name):
        """
        Return controller's action as callable.
        """
        return getattr(controller, action_name, getattr(controller, 'not_found', None))

    def _format_error_message(self, msg, with_traceback=False):
        if with_traceback:
            tb = traceback.format_exc()
            msg += '<h3>Traceback</h3>\n\n<pre>{}</pre>'.format(tb)
        return msg

    def __call__(self, environ, start_response):
        """
        Find appropriate controller for requested address.

        Return Response object that support the WSGI interface.
        """
        request = Request(environ)
        try:
            controller_name = request.get_controller_name()
            controller = self.get_controller_by_name(controller_name)
            action_name = request.get_action_name()
            action = self.get_controller_action(controller, action_name)
            if not action and controller_name != 'index':
                # call index controller for catch all unhandled pages
                controller = self.get_controller_by_name('index')
                action = self.get_controller_action(controller, 'not_found')
            if not callable(action):
                # action handler should be a callable function
                raise PageNotFound(
                    "Controller '{name}' doesn't have action '{action}'",
                    name=controller_name,
                    action=action_name
                )
            resp = action(request)
            if not isinstance(resp, Response):
                raise Exception("Controller should return Response object, but given '{}'".format(type(resp)))
        except PageNotFound as err:
            message = self._format_error_message(str(err), with_traceback=True)
            return HTTPNotFound(message)(environ, start_response)
        except Exception as err:
            message = self._format_error_message(str(err), with_traceback=True)
            return HTTPInternalServerError(message)(environ, start_response)

        return resp(environ, start_response)
