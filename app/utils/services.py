from django.db.models import Count

from app.models import Post, PostLikes


def get_all_posts() -> Post:
    return Post.objects.all().select_related('author').prefetch_related('likes')


def get_post_by_id(id: int) -> Post:
    return Post.objects.filter(id=id).first()


def create_post_likes(user_id: int, post_id: int) -> None:
    PostLikes.objects.create(user_id=user_id, post_id=post_id)


def delete_post_likes(post_id: int) -> None:
    PostLikes.objects.filter(post_id=post_id).delete()


def get_post_by_params(params: dict) -> Post:
    return Post.objects.filter(**params).exists()


def create_post(params: dict) -> None:
    Post.objects.create(**params)


def get_post_likes_by_liked_date_range(date_from, date_to) -> PostLikes:
    return PostLikes.objects.filter(liked_on__range=(date_from, date_to)). \
        values_list('post__title').annotate(Count('post')) \
        .prefetch_related('post')
