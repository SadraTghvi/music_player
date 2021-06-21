from django.shortcuts import render
from songs.models import *


def main(request):
    song = Song.objects.all()
    context = {
        "songs" : song,
    }
    return render(request, "base.html", context)

# Create your views here.

