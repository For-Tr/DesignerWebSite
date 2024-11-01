from rest_framework import serializers

from notes.models import Note


class ThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class UpdateThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
