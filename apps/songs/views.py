# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

from songs.forms import SongsForm
from songs.models import Song


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
def view_songs(request):

    output= Song.title
    return HttpResponse(output)

    