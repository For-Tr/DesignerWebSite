import random
import string

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
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
    """于文章列表中引用的嵌套序列化器"""

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'avatar'
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')
    repassword = serializers.CharField(write_only=True, style={'input_type': 'password'})

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

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        username = validated_data.get('username')

        user = User.objects.create_user(password=password, username=username, email=email)

        # 生成验证代码
        verification_code = self.generate_verification_code()

        # 在数据库中创建或更新验证记录
        verification_record, created = email_reset.objects.update_or_create(
            email_address=email,
            defaults={'vc_code': verification_code}
        )

        # 生成验证 URL
        verification_url = self.generate_verification_url(email, verification_code)

        # 发送验证邮件
        self.send_verification_email(email, verification_url)

        return user

    def generate_verification_code(self, size=32, chars=string.ascii_uppercase + string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_verification_url(self, email, verification_code):
        url = reverse('verify-email')  # 设置验证视图的 URL 名称
        verification_url = f"{settings.BASE_URL}{url}?email={email}&code={verification_code}"
        return verification_url

    def send_verification_email(self, email, verification_url):
        subject = 'PBuilder.verify'
        message = f'click this link to verify your email {verification_url}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_email_verified'] = user.is_email_verified
        return token
