# from jinja import Template
from .base import BaseView


class JinjaView(BaseView):
    """
    Jinja view.
    """

    def _load_engine(self, template_dir):
        """
        Load template engine by name and return an instance.
        """
        return None
        # return Template

    def render(self, template_name, variables=None):
        """
        Render a template with the passed variables.
        """
        return "Jinja template"
