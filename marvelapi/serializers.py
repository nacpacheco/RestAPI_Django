from rest_framework import serializers

from .models import *


class ComicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comic
        fields = ('name', 'uri')


class StorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storie
        fields = ('name', 'uri', 'type')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'uri')

class SerieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serie
        fields = ('name', 'uri')

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ('uri', 'type')

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    comic_set  =  ComicSerializer(many=True)
    storie_set =  StorieSerializer(many=True)
    event_set  =  EventSerializer(many=True)
    serie_set  =  SerieSerializer(many=True)
    url_set = UrlSerializer(many=True)
    class Meta:
        model = Character
        fields = ('name', 'description', 'modified', 'image', 'uri', 'comic_set', 'storie_set', 'event_set',
                  'serie_set', 'url_set')

