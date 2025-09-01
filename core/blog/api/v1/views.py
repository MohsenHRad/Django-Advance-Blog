from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer, PostModelSerializer
from ...models import Post


@api_view()
def postList(request):
    posts = Post.objects.filter(status=True)
    serializer = PostModelSerializer(posts, many=True)
    return Response(serializer.data)


@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)

    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({'detail': 'Post does not exist'},status=status.HTTP_404_NOT_FOUND)
