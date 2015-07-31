import os
from pythonrails import run


if __name__ == '__main__':
    project_dir = os.path.dirname(os.path.realpath(__file__))
    run(port=8500, project_dir=project_dir)
