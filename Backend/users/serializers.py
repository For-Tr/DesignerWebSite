import random
import string
import time
from smtplib import SMTPException

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db import transaction
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from notes_back import settings

from users.models import User, email_reset


# 用户序列化
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'nickname',
            'avatar',
            'mobile',
            'description'
        ]


class UserSerializers(serializers.ModelSerializer):  # 登录专用返回人员usertype的
    usertype = serializers.CharField(
        source="get_usertype_display", read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserDescSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'avatar',
            'nickname'
        ]


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='username'
    )
    repassword = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'email',
            'username',
            'password',
            'repassword',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        repassword = attrs.get('repassword')

        if password and repassword and password != repassword:
            raise serializers.ValidationError("Passwords do not match.")

        return attrs

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

    def validate_email(self, value):
        """Validate if email is already registered but not verified"""
        existing_user = User.objects.filter(email=value).first()
        if existing_user and existing_user.is_active:
            raise serializers.ValidationError("This email is already registered.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        try:
            # Remove repassword from validated_data
            validated_data.pop('repassword', None)

            email = validated_data.get('email')
            password = validated_data.get('password')
            username = validated_data.get('username')

            # Check if user exists but is not active (not verified)
            existing_user = User.objects.filter(email=email).first()
            if existing_user and not existing_user.is_active:
                # Delete existing unverified user
                existing_user.delete()

            # Create new user with is_active=False
            user = User.objects.create_user(
                password=password,
                username=username,
                email=email,
                is_active=False
            )

            # Generate verification code
            verification_code = self.generate_verification_code()

            # Create/update verification record
            try:
                verification_record, created = email_reset.objects.update_or_create(
                    email_address=email,
                    defaults={'vc_code': verification_code}
                )
            except Exception as e:
                raise serializers.ValidationError(
                    "Failed to create verification record. Please try again."
                )

            # Generate verification URL
            verification_url = self.generate_verification_url(email, verification_code)

            # Send verification email
            try:
                self.send_verification_email(email, verification_url)
            except SMTPException:
                raise serializers.ValidationError(
                    "Failed to send verification email. Please try again later."
                )
            except Exception as e:
                raise serializers.ValidationError(
                    "An error occurred while sending verification email." + str(e)
                )

            return user

        except Exception as e:
            # Rollback transaction if any error occurs
            transaction.set_rollback(True)
            raise

    def send_verification_email(self, email, verification_url):
        max_retries = 1
        retry_count = 0

        while retry_count < max_retries:
            try:
                subject = 'PBuilder.verify'
                message = f'click this link to verify your email {verification_url}'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [email]

                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False
                )
                return
            except SMTPException:
                retry_count += 1

                if retry_count == max_retries:
                    raise serializers.ValidationError(
                        "An error occurred while sending verification email.(SMTP Connect Failed)try again later"
                    ).detail

    def generate_verification_code(self, size=32, chars=string.ascii_uppercase + string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_verification_url(self, email, verification_code):
        url = reverse('verify-email')
        verification_url = f"{settings.BASE_URL}{url}?email={email}&code={verification_code}"
        return verification_url



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_email_verified'] = user.is_email_verified
        return token
