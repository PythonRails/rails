from pythonrails.response import Response


class Blogs(object):

    def index(self, request):
        return Response('Blogs home page')

    def details(self, request):
        """
        Show info about the blog.
        """
        blog_name = request.get_url_param(0)
        return Response('Show {} blog'.format(blog_name))

    def not_found(self, request):
        return Response('Page not found inside Blogs controller')
