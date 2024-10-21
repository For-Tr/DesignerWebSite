from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User


# 身份认证
class TokenAuthtication(JWTAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_TOKEN")
        if token is not None:
            print("checking token==>" + token)
            validated_token = self.get_validated_token(token)
            user = User.objects.filter(pk=validated_token['user_id']).first()
            if not token or len(user) == 0:
                raise exceptions.AuthenticationFailed("Authentication Failed!")
            else:
                print('checked')
        else:
            raise exceptions.AuthenticationFailed("Authentication Failed!")
