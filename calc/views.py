from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import movies
from django.contrib import messages
from django.contrib.auth.models import User, auth
def home(request):
    return render(request, "home.html")

def main(request):
    mov1 = movies()
    mov1.name = "The Jungle Book"
    mov1.ids = "M001"
    mov1.genre = "Adventure"
    mov1.img = "jungle.jpg"
    mov1.rating = 7.40
    
    mov2 = movies()
    mov2.name = "Lucy"
    mov2.ids = "M003"
    mov2.genre = "Thriller"
    mov2.img = "Lucy.jpg"
    mov2.rating = 6.40
    
    mov3 = movies()
    mov3.name = "Cellular"
    mov3.ids = "M004"
    mov3.genre = "Action"
    mov3.img = "Cellular.jpg"
    mov3.rating = 6.50
    
    mov4 = movies()
    mov4.name = "Frozen"
    mov4.ids = "M008"
    mov4.genre = "Musical"
    mov4.img = "frozen.jpg"
    mov4.rating = 7.50

    mov5 = movies()
    mov5.name = "The Grudge"
    mov5.ids = "M012"
    mov5.genre = "Horror"
    mov5.img = "grudge.jpg"
    mov5.rating = 5.40

    mov6 = movies()
    mov6.name = "Altered Carbon: Resleeved"
    mov6.ids = "M005"
    mov6.genre = "Anime"
    mov6.img = "alter.jpg"
    mov6.rating = 7.40

    mov7 = movies()
    mov7.name = "Joker"
    mov7.ids = "M014"
    mov7.genre = "Crime"
    mov7.img = "joker.jpg"
    mov7.rating = 8.40

    mov8 = movies()
    mov8.name = "Colonia"
    mov8.ids = "M010"
    mov8.genre = "Thriller"
    mov8.img = "colonia.jpg"
    mov8.rating = 7.10

    mov9 = movies()
    mov9.name = "Titanic"
    mov9.ids = "M017"
    mov9.genre = "Drama"
    mov9.img = "titanic.jpg"
    mov9.rating = 7.80

    mov10 = movies()
    mov10.name = "The Karate Kid"
    mov10.ids = "M018"
    mov10.genre = "Drama"
    mov10.img = "karate.jpg"
    mov10.rating = 6.20

    

    movs = [mov1, mov2, mov3, mov4, mov5, mov6, mov7, mov8, mov9, mov10]
    
    return render(request, "main.html", {'movs': movs})


def video(request):
    return render(request, "video.html")

