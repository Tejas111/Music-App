from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import album
def ind (request):
    album1 = album.objects.all()
    return render(request,'t1/index.html',{'all_albums':album1})
    #template=loader.get_template("t1/index.html")
   

def detail(request,album_id):
    album1 = get_object_or_404(album,pk=album_id)
    return render(request,'t1/detail.html',{'album':album1})

def favorite(request,album_id):
    album1= get_object_or_404(album,pk=album_id)
    try:
        s_song= album1.song_set.get(pk=request.POST['song'])
    except (KeyError):
        return render(request,'t1/detail.html',{'album':album1,'error_message':"No song is selected"})
    else:
        s_song.is_favorite=True
        s_song.save()
        return render(request,'t1/detail.html',{'album':album1})