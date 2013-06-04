"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core import mail
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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

class AccountLogin(TestCase):
    
    def test_login(self):
        url = reverse("login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        test_user = User(username='username', password=make_password('password'),email= 'email@test.com',first_name= 'first_name',last_name= 'last_name')
        test_user.save()

        data = {
            "username":"username",
            "password":"password"
        }
        response = self.client.post(url, data,)
        self.assertEqual(response.status_code, 302)

        self.assertIn('_auth_user_id', self.client.session)

        self.assertEqual(self.client.session['_auth_user_id'], test_user.pk)

class ForgotPassword(TestCase):
    def test_forgotpassword(self):
        url=reverse("password_reset")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

        test_user = User(username='username', password=make_password('password'),email='email@test.com',first_name='first_name',last_name='last_name')
        test_user.save()

        data= {
            "email":"email@test.com"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code,302)

class UserEdit(TestCase):
    
    def test_user_edit(self):
        

        test_user = User(username='username', password=make_password('password'),email='email@test.com',first_name='first_name',last_name='last_name')
        test_user.save()
        test_profile = UserProfile(user=test_user,country='DE')
        
        test_profile.save()

        logged_in = self.client.login(username="username", password="password")
        self.assertTrue(logged_in)

        url=reverse("user_edit")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

        data ={
            'first_name':'fname',
            'last_name':'lname',
            'country':'RO'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code,302)

        user_check = User.objects.get(pk=test_user.pk)
        
        self.assertEqual(user_check.first_name,data['first_name'])
        self.assertEqual(user_check.last_name,data['last_name'])
        
        profile_check = UserProfile.objects.get(pk=test_profile.pk)

        self.assertEqual(profile_check.country,data['country'])
        

      




class ProfileTest(TestCase):
    def test_profile_page(self):
        url = reverse("profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
            
        test_user = User(username='username', password=make_password('password'),email='email@test.com',first_name='first_name',last_name='last_name')
        test_user.save()        

        test_user_profile = UserProfile.objects.create(
                user=test_user,
                country="DE"
        )

        logged_in = self.client.login(username=test_user.username, password="password")
        self.assertTrue(logged_in)    

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertTrue( test_user.first_name in response.content )
        self.assertTrue( test_user.last_name in response.content )
        
    
        self.assertTrue( test_user_profile.get_country_display() in response.content )


       

