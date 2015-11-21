"""
Configuration for a project.
"""
from .tools import import_module


class Config(object):
    _data = None

    def __init__(self):
        """
        Load config for a project.
        """
        if Config._data:
            raise Exception('Config already loaded')
        Config._data = self._load_config()

    def _load_config(self):
        """
        Load project's config and return dict.

        TODO: Convert the original dotted representation to hierarchical.
        """
        config = import_module('config')
        variables = [var for var in dir(config) if not var.startswith('_')]
        return {var: getattr(config, var) for var in variables}

    @staticmethod
    def get(name, default=None):
        """
        Return variable by name from the project's config.

        Name can be a dotted path, like: 'rails.db.type'.
        """
        if '.' not in name:
            raise Exception("Config path should be divided by at least one dot")
        section_name, var_path = name.split('.', 1)
        section = Config._data.get(section_name)
        return section.get(var_path)


def get_config(name, default=None):
    """
    Return variable by name from the project's config.

    Name can be a dotted path, like: 'rails.db.type'.
    """
    return Config.get(name, default)
