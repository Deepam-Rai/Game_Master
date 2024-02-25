import logging
import sys
import importlib

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def import_class(module_name, class_name):
    try:
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        return class_
    except (ImportError, AttributeError):
        logging.error(f"Class {class_name} not found in module {module_name}.")


def import_constants(module_name):
    try:
        module = importlib.import_module(module_name + ".win_config")
        constants = {name: value for name, value in module.__dict__.items() if name.isupper()}
        return constants
    except (ImportError, AttributeError):
        logging.error(f"Could not import windows configs constants from module {module_name}.win_config.py")
