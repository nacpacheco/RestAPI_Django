from rest_framework import viewsets
from .serializers import CharacterSerializer
from .models import *


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name').select_related()
    serializer_class = CharacterSerializer
