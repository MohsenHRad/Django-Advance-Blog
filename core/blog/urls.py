from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'blog'
urlpatterns = [
    path('django/<int:pk>', views.RedirectToDjango.as_view(), name='redirect-to-django'),
    # path('cbv-index', TemplateView.as_view(template_name='index.html',extra_context={'name':'mohsen '}))
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path(
        'go-to-index',
        RedirectView.as_view(pattern_name='blog:fbv-index'),
        name='redirect-to-index'
    ),
    path('post', views.PostList.as_view(), name='view for listing posts')
]
