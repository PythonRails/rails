from jinja2 import Environment
from jinja2 import FileSystemLoader
from .base import BaseView


class JinjaView(BaseView):
    """
    Jinja view.
    """

    def _load_engine(self, template_dir):
        """
        Load template engine by name and return an instance.
        """
        return Environment(loader=FileSystemLoader(template_dir))

    def render(self, template_name, variables=None):
        """
        Render a template with the passed variables.
        """
        if variables is None:
            variables = {}
        template = self._engine.get_template(template_name)
        return template.render(**variables)

    def render_source(self, source, variables=None):
        """
        Render a source with the passed variables.
        """
        if variables is None:
            variables = {}
        template = self._engine.from_string(source)
        return template.render(**variables)
