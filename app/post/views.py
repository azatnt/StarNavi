import datetime

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.post.serializers import PostCreateSerializer, PostListSerializer
from app.utils.services import get_post_by_id, get_all_posts, create_post_likes, delete_post_likes, get_post_by_params, \
    create_post


class PostViewSet(viewsets.ViewSet):

    @action(methods=["POST"], permission_classes=(IsAuthenticated,), detail=False, url_path=r'create')
    def create_post(self, request):
        serializer_class = PostCreateSerializer(data=request.data)
        if serializer_class.is_valid():
            data = {'author': request.user, 'title': serializer_class.data.get('title'),
                    'description': serializer_class.data.get('description')
                    }
            if not get_post_by_params(params=data):
                create_post(params=data)
                return Response({"message": "Post successfully created!"}, status=status.HTTP_201_CREATED)
            return Response({"message": "Post already exists!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=["GET"], permission_classes=(IsAuthenticated,), detail=False, url_path=r'get-all')
    def all_posts(self, request):
        posts = get_all_posts()
        serialized_data = PostListSerializer(posts, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)


    @action(methods=["POST"], permission_classes=(IsAuthenticated,), detail=False, url_path=r'(?P<id>\w+)/like')
    def like_post(self, request, id):
        try:
            post = get_post_by_id(id=id)
            user = request.user
            if not user in post.likes.all():
                create_post_likes(user_id=user.id, post_id=post.id)
                return Response({"message": f"{user.username} liked {post.title}"}, status=status.HTTP_200_OK)
            return Response({"message": f"{user.username} already liked {post.title}"},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Post doesn't exist!"}, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=["POST"], permission_classes=(IsAuthenticated,), detail=False, url_path=r'(?P<id>\w+)/unlike')
    def unlike_post(self, request, id):
        try:
            post = get_post_by_id(id=id)
            user = request.user
            if user in post.likes.all():
                delete_post_likes(post_id=post.id)
                return Response({"message": f"{user.username} unliked {post.title}"}, status=status.HTTP_200_OK)
            return Response({"message": f"{user.username} already unliked {post.title}"},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Post doesn't exist!"}, status=status.HTTP_400_BAD_REQUEST)
