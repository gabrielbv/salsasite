"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login


from django.contrib.auth.models import User
from events.models import Event



class EventsTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(first_name='user1',last_name='user1',username='user1',password='pass',email='user1@test.com')
        self.user2 = User.objects.create_user(first_name='user2',last_name='user2',username='user2',password='pass',email='user2@test.com')
        self.event = Event.objects.create(title='event1',body='test event',pub_date=timezone.now(),start_date=timezone.now(),location='brasov',feature='feature test',ticket=3,slug='event1',user=self.user1)
        

    def test_list_events(self):
        response =self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'No articles yet')
        
        self.event.event_status='DRAFT'
        self.event.start_date=timezone.now()+datetime.timedelta(days=1)
        self.event.save()
        
        response =self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response,self.event.title)


        self.event.event_status='PENDING'
        self.event.start_date=timezone.now()+datetime.timedelta(days=1)
        self.event.save()
        
        response =self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response,self.event.title)    

        self.event.event_status='DENIED'
        self.event.start_date=timezone.now()+datetime.timedelta(days=1)
        self.event.save()
        
        response =self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response,self.event.title)  


        self.event.event_status='APROVED'
        self.event.start_date=timezone.now()+datetime.timedelta(days=1)
        self.event.save()
        
        response =self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,self.event.title)
        

        response =self.client.get(reverse('event_details',args=(self.event.slug,self.event.id)))
        self.assertEqual(response.status_code, 200)

    def test_add_event(self):
        url = reverse('add_event')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code,302)

        
        logged_in=self.client.login(username=self.user1.username,password='pass')
        
        

        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

        data={} 
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,200)
        self.assertFormError(response,'form','title',[u'This field is required.'])

        data={
            'title':'event create',
            'body':'test event',
            'pub_date':timezone.now().date().isoformat(),
            # strftime converts from date to string 
            'start_date':(timezone.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'location':'brasov',
            'feature':'test feature',
            'ticket':'100',
            'ticket_status':'NOWAVALIBLE'
            }
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,302)
        
        # there has to be 2 events, one from setup and one just created
        self.assertEqual(Event.objects.all().count(),2)
        new_event=Event.objects.exclude(id=self.event.id).get()

        
        urldetails=reverse('event_details',args=(new_event.slug,new_event.id))
        self.assertRedirects(response,urldetails,status_code=302)

    def test_edit_event(self):
        url = reverse('edit',args=(self.event.slug,self.event.id))
        response=self.client.get(url)
        self.assertEqual(response.status_code,302)

        self.client.login(username=self.user1.username,password='pass')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

        data={} 
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,200)
        self.assertFormError(response,'form','title',[u'This field is required.'])


        data={
            'title':'event create',
            'body':'test event',
            'pub_date':timezone.now().date().isoformat(),
            # strftime converts from date to string 
            'start_date':(timezone.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'location':'brasov',
            'feature':'test feature',
            'ticket':'100',
            'ticket_status':'NOWAVALIBLE'
            }
        
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,302)

        self.event.event_status='PENDING'
        self.event.save()
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

        self.event.event_status='APROVED'
        self.event.save()
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)

        self.event.event_status='DENIED'
        self.event.save()
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)

        self.client.logout()


        self.client.login(username=self.user2.username,password='pass')
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)

    def test_private_events(self):
        url=reverse('my_events')
        response=self.client.get(url)
        self.assertEqual(response.status_code,302)

        self.client.login(username=self.user1.username,password='pass')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'event1')
        self.assertContains(response,'Edit')

        self.event.event_status ='PENDING'
        self.event.save()
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.event.title)
        self.assertContains(response,'Edit')


        self.event.event_status ='APROVED'
        self.event.save()
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.event.title)
        self.assertNotContains(response,'Edit')

        self.event.event_status ='DENIED'
        self.event.save()
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.event.title)
        self.assertContains(response,'Edit')








        


        






  