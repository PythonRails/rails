from webob import Request as WebobRequest


class Request(WebobRequest):
    """
    Extended request object.
    """

    def get_url_controller(self):
        return self.path_info.strip('/').split('/', 1)[0] or 'index'

    def get_url_action(self):
        try:
            return self.path_info.strip('/').split('/', 2)[1]
        except IndexError:
            return 'index'

    def get_url_params(self):
        return self.path_info.strip('/').split('/')[2:]
