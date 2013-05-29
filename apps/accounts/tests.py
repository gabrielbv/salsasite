"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from accounts.models import UserProfile

class AccountTest(TestCase):
    def test_failed_registrations(self):
    
        url = reverse("register")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            "username":"foo",
            "firstname":"foo",
            "lastname":"foo",
            "email":"foo@bar.com",
            "confirm_email":"foobar@bar.com",
            "password":"foo",
            "confirm_password":"foo",
            "country":"foo",
        }
        response = self.client.post(url, data,)
        
        self.assertEqual(response.status_code, 200)

        self.assertEqual(User.objects.filter(username=data["username"]).count(), 0)

        data['confirm_email'] = data['email']
        
        data['password'] = "foobar"
        response = self.client.post(url, data,)
        self.assertEqual(User.objects.filter(username=data["username"]).count(), 0)
        

    def test_registration(self):
    
    	url = reverse("register")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            "username":"foo",
            "firstname":"foo",
            "lastname":"foo",
            "email":"foo@bar.com",
            "confirm_email":"foo@bar.com",
            "password":"foo",
            "confirm_password":"foo",
            "country": "RO",
        }
        response = self.client.post(url, data,)
        
        self.assertEqual(response.status_code, 302)

        self.assertEqual(User.objects.filter(username=data["username"]).count(), 1)
        self.assertEqual(UserProfile.objects.filter(user__username=data["username"]).count(), 1)

        profile = UserProfile.objects.get(user__username=data["username"])
        self.assertTrue(profile.country)

        logged_in = self.client.login(username=data["username"], password=data["password"])
        self.assertTrue(logged_in)