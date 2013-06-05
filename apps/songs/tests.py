"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from accounts.models import UserProfile
from songs.models import Song

class SongTest(TestCase):
    def test_add_song(self):
        url = reverse ("add_song")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        test_user = User(username='username', password=make_password('password'),email= 'email@test.com',first_name= 'first_name',last_name= 'last_name')
        test_user.save()

        test_user_profile = UserProfile.objects.create(
            user=test_user,
            country="RO")
        logged_in = self.client.login(username=test_user.username, password="password")
        self.assertTrue(logged_in)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        musicfile=open("static/test.mp3") 
        
        data = {
        "title":"foo",
        "artist":"bar",
        "genre":"salsa",
        "music_file":musicfile,
        }
        response = self.client.post(url, data,)
        self.assertEqual(response.status_code, 302)

        #self.assertEqual(User.objects.filter(username=data["username"]).count(), 1)
        self.assertEqual(Song.objects.filter(title=data["title"]).count(), 1)

        url = reverse ("add_song_confirm")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

<<<<<<< HEAD
class SongView(TestCase):
    def test_song_view(self):
        url = reverse ("song_view")
        response= self.client.get(url)
        self.assertEqual(response.status_code,302)


        test_user = User(username='username', password=make_password('password'),email= 'email@test.com',first_name= 'first_name',last_name= 'last_name')
        test_user.save()
        
        test_user_profile = UserProfile.objects.create(
            user=test_user,
            country="RO")
        logged_in = self.client.login(username=test_user.username, password="password")
        self.assertTrue(logged_in)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



=======
    def test_edit_song(self):
        
        url = reverse ("song_edit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
>>>>>>> 6f3cee930569873dc41cb911ea2f424e3dbc1eac

        
