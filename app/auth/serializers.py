from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer


class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username"""

    email = None

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "username": self.validated_data.get("username", ""),
        }


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""

    email = None