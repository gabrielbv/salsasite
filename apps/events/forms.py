from django import forms 
from events.models import Event


class EventForm(forms.ModelForm):
    
    class Meta:
        model=Event
        fields = ['title','body','pub_date','start_date','location','feature','ticket','ticket_status']
