from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render , render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from songs.models import Song
from purchases.forms import PurchaseCode

from accounts.forms import UserForm,UserEdit
from accounts.models import UserProfile



# Create your views here.

@login_required

def purchase(request,song_id ):
    
    form = PurchaseCode()

    try:

        song = Song.objects.get(pk=song_id)

    except Song.DoesNotExist:

        raise Http404

    return render(request, 'purchases/purchase.html',{'form':form})