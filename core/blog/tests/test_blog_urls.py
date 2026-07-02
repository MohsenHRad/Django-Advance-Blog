from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog.views import IndexView, PostListView, PostDetailView


# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_blog_index_url_resolver(self):
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_blog_post_list_url_resolver(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_blog_post_detail_url_resolver(self):
        url = reverse('blog:post-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class,PostDetailView)
