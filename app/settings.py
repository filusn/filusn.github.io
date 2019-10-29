import os


def get_parent_dir(path):
    """Return the parent of a directory."""
    return os.path.abspath(os.path.join(path, os.pardir))


APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = get_parent_dir(APP_DIR)

FREEZER_DESTINATION = PROJECT_ROOT

FREEZER_REMOVE_EXTRA_FILES = False
