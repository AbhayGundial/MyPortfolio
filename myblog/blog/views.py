from rest_framework import viewsets
from .serializer import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    serializer_class = PostSerializer
    

# class PostDetail(generic.DetailView):
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return HttpResponse(self.object)