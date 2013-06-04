# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.contrib import messages

from songs.forms import SongsForm
from songs.forms import Song


@login_required
def add_song(request):

    form = SongsForm()
    if request.method == "POST":
        
    	form = SongsForm(request.POST ,request.FILES)
        
        if form.is_valid():
            
            song = form.save()
            
            
            return HttpResponseRedirect(reverse("add_song_confirm"))
        
    return render(request, 'songs/add_song.html', {'form': form})
    
@login_required
def add_song_confirm(request):

    return render(request, 'songs/add_song_confirm.html')


@login_required
def song_edit(request, song_id):

    try:
        song = Song.objects.get(pk=song_id)


    except Song.DoesNotExist:

        raise Http404

    form = SongsForm(instance=song)
    if request.method == "POST":

        form = SongsForm(request.POST, request.FILES, instance=song)
            
        if form.is_valid():

            song=form.save()

            messages.success(request, 'Song details updated.')

            return HttpResponseRedirect(reverse("song_edit", args=[song_id]))

    return render(request, 'songs/song_edit.html', {'form': form})
    