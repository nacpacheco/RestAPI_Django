from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Character
from .serializers import CharacterSerializer

# Testing MarvelAPI app

class PrivateIngredientsApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    # Tests retrieving character list
    def test_get_character_list(self):
        url = reverse('FullCharacterViewSet-list')
        res = self.client.get(url)
        characters = Character.objects.all().order_by('name').select_related()
        serializer = CharacterSerializer(characters, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

