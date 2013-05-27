# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from accounts.forms import UserForm
from django.shortcuts import render

def register(request):
    

    if request.method == "POST":
            
        return HttpResponseRedirect(reverse("register"))
    form = UserForm()    
    return render(request, 'accounts/register.html', {'form': form})
