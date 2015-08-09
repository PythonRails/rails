from pythonrails.response import Response


class Articles(object):

    def index(self, request):
        return Response('Articles home page')
