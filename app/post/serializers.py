from rest_framework import serializers

from app.models import Post, User


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'description']
        extra_kwargs = {'title': {'required': True}}
        extra_kwargs = {'description': {'required': True}}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PostListSerializer(PostCreateSerializer):
    author = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.all().count()

    class Meta(PostCreateSerializer.Meta):
        fields = PostCreateSerializer.Meta.fields + ['author', 'likes']