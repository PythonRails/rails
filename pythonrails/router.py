from webob import Request, Response


class Router(object):
    """
    Main project router that calls appropriate controller.
    """

    def __call__(self, environ, start_response):
        """
        Find appropriate controller for requested address.

        Returns Response object.
        """
        resp = Response(body='Hello, it works!')
        return resp(environ, start_response)
