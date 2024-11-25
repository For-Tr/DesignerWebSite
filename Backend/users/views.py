from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.auth import TokenAuthtication
from users.models import User, email_reset
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from users.serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer, UserSerializer
from users.permissions import IsSelfOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
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

    if not email or not code:
        return Response({
            'detail': 'Email and verification code are required'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        verification_record = email_reset.objects.get(email_address=email, vc_code=code)
        user = User.objects.get(email=email)
        user.is_email_verified = True
        user.is_active = True
        user.save()

        return Response({
            'detail': 'Email verification successful'
        }, status=status.HTTP_200_OK)

    except email_reset.DoesNotExist:
        return Response({
            'detail': 'Invalid or expired verification code'
        }, status=status.HTTP_400_BAD_REQUEST)

    except MultipleObjectsReturned:
        return Response({
            'detail': 'Email already registered'
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'detail': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user

            if not user.is_email_verified:
                return Response(
                    {'detail': 'Email not verified. Please verify your email first.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': str(user.username)
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            if 'No active account found' in str(e):
                return Response(
                    {'detail': 'Invalid credentials.' + str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {'detail': 'Login failed. Please try again.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def info(request):
    try:
        email = request.GET.get('email')
        if not email:
            return Response(
                {'detail': 'Email parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response(
            {'detail': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'detail': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def edit_user(request):
    try:
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            # Handle password separately if it's being updated
            if 'password' in request.data:
                serializer.validated_data['password'] = make_password(request.data['password'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    except Exception as e:
        return Response(
            {'detail': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )