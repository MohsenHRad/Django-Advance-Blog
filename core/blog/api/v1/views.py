from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import PostModelSerializer, CategorySerializer
from ...models import Post, Category


class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    Retrieving a list of Posts and Creating a new post
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostModelSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostModelSerializer
    queryset = Post.objects.filter(status=True)


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostModelSerializer
    queryset = Post.objects.filter(status=True)

    @action(methods=['get'], detail=False)
    def get_Ok(self,request):
        return Response({'detail': 'Every thing is OK'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=True)

    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     post_object = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_object)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def update(self, request, pk=None):
    #     post_obj = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(post_obj, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #
    # def partial_update(self, request, pk=None):
    #     post_obj = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.serializer_class(instance=post_obj, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #
    # def destroy(self, request, pk=None):
    #     post_obj = get_object_or_404(self.queryset, pk=pk)
    #     post_obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def get(self, request):
    #     """ Retrieving a list of Posts """
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     """ Creating a new post with provided data. """
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostModelSerializer
#     queryset = Post.objects.filter(status=True)
#
#     # lookup_field = 'id'
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.put(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# def get(self, request, id):
#     """ retrieving the post data"""
#     post = get_object_or_404(Post, pk=id, status=True)
#     serializer = self.serializer_class(post)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)

# def put(self, request, id):
#     """ editing the post data"""
#     post = get_object_or_404(Post, pk=id, status=True)
#     serializer = self.serializer_class(post, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def delete(self, request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     post.delete()
#     return Response({'detail': 'Item has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


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


class PostListGeneric(ListAPIView, ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostModelSerializer
    queryset = Post.objects.filter(status=True)
