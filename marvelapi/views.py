from rest_framework import viewsets, generics
from .serializers import *
from .models import *


class FullCharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name').select_related()
    serializer_class = CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Character.objects.all().filter(id=id).select_related()

class ComicViewSet(viewsets.ModelViewSet):
    serializer_class = ComicSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Comic.objects.all().filter(character_id=id)

class StorieViewSet(viewsets.ModelViewSet):
    serializer_class = StorieSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Storie.objects.all().filter(character_id=id)

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Event.objects.all().filter(character_id=id)

class SerieViewSet(viewsets.ModelViewSet):
    serializer_class = SerieSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Serie.objects.all().filter(character_id=id)

