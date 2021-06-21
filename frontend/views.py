from django.shortcuts import render
from django.http import HttpResponse
from songs.models import *


def main(request):
    song = Song.objects.all()
    context = {
        "songs" : song,
    }
    return render(request, "base.html", context)


def song_with_id(request,pk):
    song_filtered_by_id = Song.objects.get(id=pk)
    context = {
        "songs": song_filtered_by_id
    }
    return render(request, "songs.html", context)

# Create your views here.

