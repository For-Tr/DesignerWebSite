from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from users.models import User


class Text(models.Model):
    order_num = models.PositiveIntegerField(blank=False, null=False)
    text = models.CharField(max_length=500, blank=False, null=False)


class Pic(models.Model):
    order_num = models.PositiveIntegerField(blank=False, null=False)
    pic = models.ImageField(upload_to='pic/', null=False)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    media_type = models.CharField(max_length=10, choices=[('image', '图片'), ('video', '视频')], default='image')


class Note(models.Model):
    user = models.ForeignKey(to=User, related_name='note', on_delete=models.SET,
                             blank=True, null=True)

    temp = models.CharField(max_length=10, default="Mult")
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    text = models.ManyToManyField(Text, blank=True, related_name="text_note")
    pic = models.ManyToManyField(Pic, blank=True, related_name="pic_note")


class AccessLog(models.Model):
    ip_address = models.CharField(max_length=50)
    access_time = models.DateTimeField()
    author = models.ForeignKey(to=User, related_name='log', on_delete=models.SET,
                               blank=True, null=True)

    def __str__(self):
        return f"AccessLog - IP: {self.ip_address}, Time: {self.access_time}, Author: {self.author}"
