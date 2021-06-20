from django.shortcuts import render


def main(request):
    return render(request,"base.html")

# Create your views here.


# TODO: 1.model for songs/2.styling for cards in cards.html