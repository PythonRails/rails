from wsgiref.simple_server import make_server
from wsgiref.simple_server import demo_app


def run(host='127.0.0.1', port=8000):
    """
    Run web server.
    """
    print "Server run on {}:{}".format(host, port)
    server = make_server(host, port, demo_app)
    server.serve_forever()
