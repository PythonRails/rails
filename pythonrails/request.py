from webob import Request as WebobRequest


class Request(WebobRequest):
    """
    Extended request object.
    """

    def get_controller_name(self):
        """
        Return controller name based on query string.
        """
        return self.path_info.strip('/').split('/', 1)[0] or 'index'

    def get_action_name(self):
        """
        Return action name based on query string.
        """
        try:
            return self.path_info.strip('/').split('/', 2)[1]
        except IndexError:
            return 'index'

    def get_url_params(self):
        """
        Return all parameters that placed after controller and action name in query string.
        """
        return self.path_info.strip('/').split('/')[2:]
