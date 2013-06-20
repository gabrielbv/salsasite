from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from songs.models import Song
from purchases.forms import PurchaseCode
from purchases.models import Purchase




# Create your views here.

@login_required

def purchase(request,song_id ):
    
    form = PurchaseCode()

    try:

        song = Song.objects.get(pk=song_id)

    except Song.DoesNotExist:

        raise Http404


    if Purchase.objects.filter(user=request.user, song=song):


    	return HttpResponseRedirect(reverse("down", args=[song.id]))


    if request.method == "POST":

	    purchase = Purchase.objects.create(
	    
	    user=request.user,
	    song=song
	    )

	    return HttpResponseRedirect(reverse("down", args=[song.id]))

    return render(request, 'purchases/purchase.html',{'form':form})

@login_required

def download(request, song_id):

	try:

		song = Song.objects.get(pk=song_id)

	except Song.DoesNotExist:

		raise Http404
	
	if not Purchase.objects.filter(user=request.user, song=song):

		raise Http404

	response = HttpResponse(song.music_file.read(), content_type='audio/mp3')
	response['Content-Disposition'] = 'attachment; filename="%s"' % (song.music_file.name)

	return response