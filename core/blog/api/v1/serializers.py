from rest_framework import serializers

from accounts.models import Profile
from blog.models import Post, Category


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class PostModelSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    # category = serializers.SlugRelatedField(many=False, slug_field='name',queryset=Category.objects.all())
    # category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "snippet",
            "category",
            "author",
            "status",
            "created_date",
            "published_date",
            "relative_url",
            "absolute_url",
        ]

        read_only_fields = ["author"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep["state"] = "list"
        if request.parser_context.get("kwargs").get("pk"):
            rep["state"] = "single"
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content")
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data

        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "status"]
