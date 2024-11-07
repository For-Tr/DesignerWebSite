from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from users.models import User


class Text(models.Model):
    order_num = models.PositiveIntegerField(blank=False, null=False)
    text = models.CharField(max_length=200, blank=False, null=False)


class Pic(models.Model):
    order_num = models.PositiveIntegerField(blank=False, null=False)
    pic = models.ImageField(upload_to='pic/', null=False)



class Note(models.Model):
    user = models.ForeignKey(to=User, related_name='note', on_delete=models.SET,
                             blank=True, null=True)

    temp = models.CharField(max_length=10, default="Mult")
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    text = models.ManyToManyField(Text, blank=True, related_name="text_note")
    pic = models.ManyToManyField(Pic, blank=True,  related_name="pic_note")

