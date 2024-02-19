from rest_framework import serializers
from .models import Note, NoteChange

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['owner']


class NoteChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteChange
        fields = '__all__'
