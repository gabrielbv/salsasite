"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase


class MusicManage(TestCase):
    def test_music_manage(self):
        url = reverse ("music_manage")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


