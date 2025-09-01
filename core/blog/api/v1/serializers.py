from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'status', 'created_date', 'published_date']
        # read_only_fields = ['id']
