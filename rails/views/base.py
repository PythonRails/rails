

class BaseView(object):
    """
    Base View interface.

    Defines an external interface for all Views.
    """
    _template_dir = None
    _engine = None

    def __init__(self, template_dir):
        self._template_dir = template_dir
        self._engine = self._load_engine(template_dir)

    def _load_engine(self, template_dir):
        """
        Load template engine by name and return an instance.
        """
        raise Exception("Not implemented")

    def render(self, template_name, variables=None):
        """
        Render a template with the passed variables.
        """
        raise Exception("Not implemented")
