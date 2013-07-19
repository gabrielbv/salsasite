from django.db import models

from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    pub_date = models.DateField('date published')
    start_date = models.DateTimeField ()
    location = models.CharField (max_length = 200)
    feature = models.CharField(max_length = 200)
    ticket = models.PositiveSmallIntegerField()

    TICKETS = (
        ('NOWAVALIBLE', 'Now Available'),
        ('NOTAVALIBLE', 'Coming Soon'),
        )
    ticket_status = models.CharField(max_length =20 , choices=TICKETS, default='NOTAVALIBLE')

    user = models.ForeignKey (User)

    STATS = (
        ('DRAFT', 'Draft'),
        ('PENDING', 'Pending'),
        ('APROVED', 'Aproved'),
        ('DENIED','Denied'),
        )
    event_status=models.CharField(max_length=20,choices=STATS,default='DRAFT')

    def __unicode__(self):
        return self.title

