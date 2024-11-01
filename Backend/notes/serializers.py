from rest_framework import serializers

from notes.models import Note, Pic, Text
from users.serializers import UserDescSerializer


class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class ThingSerializer(serializers.ModelSerializer):
    pic = PicSerializer(many=True)
    text = TextSerializer(many=True)
    user = UserDescSerializer()

    class Meta:
        model = Note
        fields = '__all__'


class UpdateThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
