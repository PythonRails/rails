from ..tools import import_module


class View(object):
    """
    General View layer.

    Hides details of implementation of concrete template engine.
    """
    _instance = None

    def __init__(self, template_engine_name, template_dir):
        # init only once
        if View._instance:
            raise Exception('Use View.render() to render template')
        View._instance = self._load_view(template_engine_name, template_dir)

    def _load_view(self, template_engine_name, template_dir):
        """
        Load view by name and return an instance.
        """
        file_name = template_engine_name.lower()
        class_name = "{}View".format(template_engine_name.title())
        try:
            view_module = import_module("rails.views.{}".format(file_name))
        except ImportError:
            raise Exception("Template engine '{}' not found in 'rails.views'".format(file_name))
        view_class = getattr(view_module, class_name)
        return view_class(template_dir)

    @staticmethod
    def render(template_name, variables=None):
        """
        Render a template with the passed variables.
        """
        return View._instance.render(template_name, variables)


def render_template(template_name, variables=None):
    """
    Render a template with the passed variables.

    Used a template engine that defined in a project settings.
    """
    return View.render(template_name, variables)
