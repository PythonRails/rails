"""
Set of useful tools.
"""
import sys


def import_module(module_name):
    """
    Improt module and return it.
    """
    __import__(module_name)
    module = sys.modules[module_name]
    return module
