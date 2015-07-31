from pythonrails.response import Response


class Index(object):

    def index(self, request):
        return Response("Website home page")

    def not_found(self, request):
        return Response("Handle all pages near the Index controller. Now requested {}".format(request.path))
