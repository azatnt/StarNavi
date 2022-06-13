from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView

class Login(LoginView):
    pass

class Register(RegisterView):
    email = None
    pass