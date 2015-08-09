from pythonrails.response import Response


class Blogs(object):

    def index(self, request):
        return Response('Blogs home page')

    def not_found(self, request):
        return Response('Page not found inside Blogs controller')
