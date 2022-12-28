from django.http import HttpResponse
from django.views import generic

from blog.models import Post

class PostView(generic.ListView):
    # Vamos renderizar a ListView para alimentar o index.html em post_list
    queryset = Post.object.filter(status = 1).order_by('-created_on') # ordenará decrescente
    template_name = "index.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"