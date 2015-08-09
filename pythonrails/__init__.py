import os
from wsgiref.simple_server import make_server
from pythonrails.router import Router


def run(host='127.0.0.1', port=8000, project_dir=os.getcwd()):
    """
    Run web server.
    """
    print "Server running on {}:{}".format(host, port)
    app_router = Router(project_dir=project_dir)
    server = make_server(host, port, app_router)
    server.serve_forever()
