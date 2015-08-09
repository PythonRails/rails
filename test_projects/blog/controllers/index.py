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

        For example, you can open page '/index/something' - to go to this method.
        """
        return Response("Handle all pages near the Index controller. Now requested {}".format(request.path))
