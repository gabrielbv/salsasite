from django import forms 
from events.models import Event


class EventForm(forms.ModelForm):
    
    STATS = (
        ('', 'Select me'),
        ('DRAFT', 'Draft'),
        ('PENDING', 'Pending'),
        )

    event_status=forms.ChoiceField(widget=forms.RadioSelect, choices =STATS,required =False)
    
    class Meta:
        model=Event
        fields = ['title','body','pub_date','start_date','location','feature','ticket','ticket_status','event_status']
        
