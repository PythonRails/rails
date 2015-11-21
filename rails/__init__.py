from wsgiref.simple_server import make_server
from .router import Router


def run(host='127.0.0.1', port=8000):
    """
    Run web server.
    """
    print("Server running on {}:{}".format(host, port))
    app_router = Router()
    server = make_server(host, port, app_router)
    server.serve_forever()
