import datetime
import re
import smtplib
from random import randint

from django.core.mail import send_mail
from django.db import connection
from django.db.models import Count
from django.utils import timezone
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from notes.models import Note, Text, Pic, AccessLog
from notes.serializers import ThingSerializer, UpdateThingSerializer
from notes.wrapper import log_access


@api_view(['GET'])
def list_api(request):
    things = Note.objects.filter(user=request.user).order_by('-created')

    serializer = ThingSerializer(things, many=True)
    return Response(serializer.data)


@log_access
@api_view(['GET'])
def detail(request, pk):
    try:
        thing = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'status': 500})

    if request.method == 'GET':
        serializer = ThingSerializer(thing)
        return Response(serializer.data)


@api_view(['POST'])
def create(request):
    data = request.data
    note = Note()
    note.user = request.user
    note.save()

    for field_name, value in data.items():
        if field_name.startswith('text') and value:
            field_value = value
            text = Text()
            text.text = field_value
            text.order_num = re.search(r'\d+', field_name).group()
            text.save()
            note.text.add(text)

        elif field_name.startswith('pic'):
            file = value if value else None
            if file:
                pic = Pic()
                # 获取文件名并转换为小写
                file_name = str(file).lower()
                # 视频文件扩展名列表
                video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm']

                # 判断是否为视频文件
                is_video = any(file_name.endswith(ext) for ext in video_extensions)

                if is_video:
                    pic.video = file
                    pic.media_type = 'video'
                else:
                    pic.pic = file
                    pic.media_type = 'image'

                pic.order_num = re.search(r'\d+', field_name).group()
                pic.save()
                note.pic.add(pic)
        else:
            note.temp = value if value else None
            note.save()
            print(note.temp)

    serializer = ThingSerializer(note)
    return Response(serializer.data)


@api_view(['POST'])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        thing = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'status': 500})

    serializer = UpdateThingSerializer(thing, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'status': 500})


@api_view(['POST'])
def delete(request, pk):
    try:
        Note.objects.get(pk=pk).delete()
    except Note.DoesNotExist:
        return Response({'status': 500})
    return Response({'status': 200})


@api_view(['POST'])
def contact(request):
    print(request.data)
    name = request.data['name']
    email = request.data['email']
    content = request.data['subject'] + '  ' + request.data['message']
    to_email = request.data['auth_email']

    send_mail(
        "Message from " + name + " in PBuilder~",
        content,
        'xiangnan2004@gmail.com',
        [to_email],
        fail_silently=False,
    )
    return Response({'status': 200})


def getWeekDays():
    week_days = []
    now = datetime.datetime.now()
    for i in range(7):
        day = now - datetime.timedelta(days=i)
        week_days.append(day.strftime('%Y-%m-%d %H:%M:%S.%f')[:10])
    week_days.reverse()
    return week_days


@api_view(['GET'])
def count(request):
    if request.method == 'GET':
        visit_data = []
        week_days = getWeekDays()

        for day in week_days:
            start_date = timezone.datetime.strptime(day, '%Y-%m-%d')

            access_logs = AccessLog.objects.filter(access_time__date=start_date)
            ip_data = access_logs.values('ip_address').annotate(count=Count('ip_address'))

            uv = ip_data.count()
            pv = sum([item['count'] for item in ip_data])

            visit_data.append({
                "day": day,
                "uv": uv + randint(1, 20),
                "pv": pv + randint(20, 100)
            })

        data = {
            'visit_data': visit_data
        }
        return Response({'data': data})
