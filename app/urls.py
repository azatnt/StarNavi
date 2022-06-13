from rest_framework.routers import DefaultRouter

from app.post.views import PostViewSet
from app.analytics.views import AnalyticsViewSet

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("", AnalyticsViewSet, basename="analytics")


urlpatterns = router.urls