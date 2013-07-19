# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect ,Http404
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse


from events.models import Event
from events.forms import EventForm
from accounts.models import User


def add_event(request):

    if request.method == 'POST':

        form=EventForm(request.POST)
        if form.is_valid():
            event=form.save(commit=False)
            event.user=request.user
            print (event.user)
            form.save()
            return HttpResponseRedirect ('/events/add/')
    else:
        form=EventForm()

    return render(request,'events/add_event.html',{'form':form,}) 

def list(request):

   
    events=Event.objects.filter(start_date__gte=timezone.now(),pub_date__lte=timezone.now(),event_status="APROVED").order_by('start_date')

    return render (request,'events/event_list.html',{'events':events})

def event_view(request,event_id):
    try:
        event=Event.objects.get(pk=event_id)
    except Event.DoesNotExist:

        raise Http404

    return render(request,'events/details.html',{'event':event})

def event_edit(request,event_id):

    
    try:
        event=Event.objects.get(pk=event_id)

    except Event.DoesNotExist:
        raise Http404

    
    form=EventForm(instance =event)
    if request.method == 'POST':

       
        if form.is_valid():
                       
            form.save()
            return HttpResponseRedirect(reverse('event_edit',args=[event_id]))
    
    return render(request,'events/event_edit.html',{'form':form,}) 

