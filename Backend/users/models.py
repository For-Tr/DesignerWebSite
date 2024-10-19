from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    email = models.EmailField(
        ('email address'),

        max_length=100,
        unique=True,
    )
    is_email_verified = models.BooleanField(verbose_name="邮箱是否验证", default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'


class email_reset(models.Model):
    email_address = models.EmailField(null=False,unique=True) #邮箱地址唯一的
    vc_code = models.CharField(max_length=64,null=False) #随机验证码
    send_time = models.DateTimeField(auto_now=True)  #邮箱发送时间


