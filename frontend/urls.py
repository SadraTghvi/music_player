from django.urls import path, include
from frontend.views import *


urlpatterns = [
    path("", main, name="main"),
    path("song/<int:pk>",song_with_id,name="song")
]


app_name = "songs"
