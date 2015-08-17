from webob import Request as WebobRequest


class Request(WebobRequest):
    """
    Represent user request.

    It contain query string, request method (get, post, put, delete) and more.
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
        Return all parameters that placed after controller and action names in url.
        """
        return self.path_info.strip('/').split('/')[2:]

    def get_url_param(self, index, default=None):
        """
        Return url parameter with given index.

        Args:
        - index: starts from zero, and come after controller and
          action names in url.
        """
        params = self.get_url_params()
        return params[index] if index < len(params) else default

    @property
    def is_ajax(self):
        """
        Check is it an AJAX request.
        """
        return self.is_xhr
