from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from notes.models import Note
from notes.serializers import ThingSerializer, UpdateThingSerializer


@api_view(['GET'])
def list_api(request):

    things = Note.objects.all().order_by('-created')

    serializer = ThingSerializer(things, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        thing = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'status': 500})

    if request.method == 'GET':
        serializer = ThingSerializer(thing)
        return Response(serializer.data)


@api_view(['POST'])
def create(request):
    print(request.data)
    serializer = ThingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
    return Response({'status': 500})


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
