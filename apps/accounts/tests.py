"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class AccountTest(TestCase):
    def test_registration(self):
    
    	url = reverse("register")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            "username":"foo",
            "firstname":"foo",
            "lastname":"foo",
            "email":"foo",
            "confirm_email":"foo",
            "password":"foo",
            "confirm_password":"foo",
            "country":"foo",
        }
        response = self.client.post(url, data,)
        
        self.assertEqual(response.status_code, 302)

        self.assertEqual(User.objects.filter(username=data["username"]).count(),1)


