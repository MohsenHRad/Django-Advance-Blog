from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView, DetailView

from .models import Post

# Function Base View show a template
'''def indexView(request):
    """
    A function based view to show index page.
    """
    context = {
        'name': 'ali'
    }
    return render(request, 'index.html', context)
'''


class IndexView(TemplateView):
    """
    A class base view to show index page.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'mohsen'
        context['posts'] = Post.objects.all()
        return context


'''
FBV for redirect
from django.shortcuts import redirect
def redirectToDjango(request):
    return redirect('https://www.djangoproject.com/')
'''


class RedirectToDjango(RedirectView):
    url = "https://www.djangoproject.com/"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    # queryset = Post.objects.all()
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    # queryset = super().get_queryset()
    # return queryset.filter(status=True)


class PostDetailView(DetailView):
    model = Post
