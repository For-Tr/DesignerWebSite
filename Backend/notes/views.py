import re
import smtplib

from django.core.mail import send_mail
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from notes.models import Note, Text, Pic
from notes.serializers import ThingSerializer, UpdateThingSerializer


@api_view(['GET'])
def list_api(request):
    things = Note.objects.all().order_by('-created')

    serializer = ThingSerializer(things, many=True)
    return Response(serializer.data)


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
            # 处理图片数据
            file = value if value else None
            if file:
                pic = Pic()
                pic.pic = file
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
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Note.objects.filter(id__in=ids_arr).delete()
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
