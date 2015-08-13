from pythonrails.response import Response


class BlogArticles(object):

    def index(self, request):
        return Response('Blog articles home page')
