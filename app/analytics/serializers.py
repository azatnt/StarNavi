from rest_framework import serializers

from app.models import Post


class AnalyticsSerializer(serializers.Serializer):
    post_title = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_post_title(self, obj):
        return obj[0]

    def get_like_count(self, obj):
        return f"liked {obj[1]} times"

    class Meta:
        model = Post
        fields = ['post_title', 'like_count']