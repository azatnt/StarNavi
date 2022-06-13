from django.utils import timezone

from app.models import User



class UpdateLastRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id) \
                           .update(last_request=timezone.now())