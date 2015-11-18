

class PageNotFound(Exception):

    def __init__(self, msg, error_code=None, **kwargs):
        self.msg = msg
        self.placeholders = kwargs

    def __str__(self):
        return self.msg.format(**self.placeholders)
