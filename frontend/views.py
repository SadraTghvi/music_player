from django.shortcuts import render
from songs.models import *


def main(request):
    song = Song.objects.all()
    context = {
        "songs" : song,
    }
    return render(request, "base.html", context)


def song_with_id(request,id):
    return render(request, "base.html")

# Create your views here.

