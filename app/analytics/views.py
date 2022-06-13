from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.analytics.serializers import AnalyticsSerializer
from app.utils.helpers import check_date_format
from app.utils.services import get_post_likes_by_liked_date_range


class AnalyticsViewSet(viewsets.ViewSet):
    @action(methods=["GET"], permission_classes=(IsAuthenticated,), detail=False, url_path=r'analytics')
    def analytics(self, request):
        if request.GET.get('date_from') is None or request.GET.get('date_to') is None:
            return Response({"message": "date_from or date_to doesn't set in params"}, status=status.HTTP_400_BAD_REQUEST)
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if check_date_format(date_from) and check_date_format(date_to):
            posts = get_post_likes_by_liked_date_range(date_from=date_from, date_to=date_to)
            serialized_data = AnalyticsSerializer(posts, many=True).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response({"message": "Incorrect data format, it should be YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)
