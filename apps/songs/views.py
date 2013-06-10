# Create your views here.
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render , render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.template import Context, loader


from accounts.models import UserProfile
from django.contrib import messages


from accounts.models import UserProfile
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

def song_view(request,song_id ):
    
    try:

        song = Song.objects.get(pk=song_id)

    except Song.DoesNotExist:

        raise Http404


    return render(request, 'songs/song.html',{'song':song})
  
	
def index(request):
    music_list = Song.objects.order_by('artist')
    template = loader.get_template('songs/index.html')
    context = Context({
        'music_list': music_list
    })
    return HttpResponse(template.render(context))


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

#def song_view_backbone(request)