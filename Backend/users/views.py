from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User, email_reset
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from users.serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer
from users.permissions import IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]

        return super().get_permissions()

@api_view(['GET'])
def verify_email(request):
    email = request.GET.get('email')
    code = request.GET.get('code')

    try:
        verification_record = email_reset.objects.get(email_address=email, vc_code=code)
    except email_reset.DoesNotExist:
        # 验证记录不存在，可以显示错误信息或重定向到错误页面
        return Response({
        'status': 500,
        'msg': '验证邮件失效，请重新注册',

    })
    except MultipleObjectsReturned:
        # 查询到多条记录，提示“邮箱已注册过”或其他适当的错误信息
        error_message = "邮箱已注册过"
        return render(request, 'error.html', {'error_message': error_message})

    # 更新用户的邮箱验证状态
    user = User.objects.get(email=email)
    user.is_email_verified = True
    user.save()

    # 验证成功，可以重定向到成功页面或其他操作
    return Response({
        'status': 201,
        'msg': '验证成功',

    })





class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user

        if not user.is_email_verified:
            return Response({'detail': '邮箱未验证，无法登录。'}, status=401)

        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data)