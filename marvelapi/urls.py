from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'characters', views.FullCharacterViewSet, basename='FullCharacterViewSet')
router.register(r'^characters/(?P<id>.+)/$', views.CharacterViewSet, base_name='Character')
router.register(r'^characters/(?P<id>.+)/comics', views.ComicViewSet, base_name='Comics')
router.register(r'^characters/(?P<id>.+)/stories', views.StorieViewSet, base_name='Storie')
router.register(r'^characters/(?P<id>.+)/events', views.EventViewSet, base_name='Events')
router.register(r'^characters/(?P<id>.+)/series', views.SerieViewSet, base_name='Series')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]