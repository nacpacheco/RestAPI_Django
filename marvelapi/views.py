from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from rest_framework.exceptions import NotFound

# Contém todas as ViewSets que fazem a busca no banco de dados conforme a requisição API e enviam ao Serializer

# /characters/
class FullCharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name').select_related()
    serializer_class = CharacterSerializer

# /characters/{id}
class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        result =  Character.objects.all().filter(id=id).select_related()
        if result:
            return result
        else:
            raise NotFound()

# /characters/{id}/comics
class ComicViewSet(viewsets.ModelViewSet):
    serializer_class = ComicSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        result = Comic.objects.all().filter(character_id=id)
        if result:
            return result
        else:
            raise NotFound()

# /characters/{id}/stories
class StorieViewSet(viewsets.ModelViewSet):
    serializer_class = StorieSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        result = Storie.objects.all().filter(character_id=id)
        if result:
            return result
        else:
            raise NotFound()

# /characters/{id}/events
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        result = Event.objects.all().filter(character_id=id)
        if result:
            return result
        else:
            raise NotFound()

# /characters/{id}/series
class SerieViewSet(viewsets.ModelViewSet):
    serializer_class = SerieSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        result = Serie.objects.all().filter(character_id=id)
        if result:
            return result
        else:
            raise NotFound()

