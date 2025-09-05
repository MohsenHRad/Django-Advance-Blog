from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostModelSerializer
from ...models import Post


class PostList(APIView):
    """
    Retrieving a list of Posts and Creating a new post
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostModelSerializer

    def get(self, request):
        """ Retrieving a list of Posts """
        posts = Post.objects.filter(status=True)
        serializer = PostModelSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Creating a new post with provided data. """
        serializer = PostModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostModelSerializer

    def get(self, request, id):
        """ retrieving the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """ editing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail': 'Item has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def postList(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(status=True)
#         serializer = PostModelSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostModelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     if request.method == 'GET':
#         serializer = PostModelSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PostModelSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response({'detail': 'Item has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# try:
#     post = Post.objects.get(pk=id)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)
# except Post.DoesNotExist:
#     return Response({'detail': 'Post does not exist'},status=status.HTTP_404_NOT_FOUND)
