from django.shortcuts import render
from app.models import Team, Player

# Create your views here.

def index_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def record_view(request):
    context = {
        "information": Team.objects.all()
    }
    return render(request, "record.html", context)

def player_view(request):
    context = {
        "roster": Player.objects.all()
    }
    return render(request, "player.html", context)
