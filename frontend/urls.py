from django.urls import path, include
from frontend.views import *


urlpatterns = [
    path("", main, name="main"),
    path("song/<int:id>",song_with_id,name="song")
]


app_name = "songs"
