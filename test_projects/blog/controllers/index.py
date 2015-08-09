from pythonrails.response import Response


class Index(object):
    """
    Index controller is a root project controller.

    With this controller you can show welcome page and handle all non-existing pages.
    """

    def index(self, request):
        """
        Show welcome page of the project.
        """
        return Response("Website home page")

    def not_found(self, request):
        """
        Handle all pages that doesn't have an action inside this controller.

        You can open page '/index/something' or '/something' to see this page.
        """
        return Response("Handle all pages in the Index controller. Requested page: {}".format(request.path))
