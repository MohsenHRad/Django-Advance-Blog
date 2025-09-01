from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import PostForm
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


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    # queryset = Post.objects.all()
    permission_required = 'blog.view_post'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    ordering = 'id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    # queryset = super().get_queryset()
    # return queryset.filter(status=True)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


'''class PostCreateView(FormView):
    template_name = 'blog/contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    # fields = '__all__'
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'


@api_view()
def api_post_list_view(request):
    return Response({'name':'mohsen'})
