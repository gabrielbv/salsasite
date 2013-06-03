from django.contrib import admin

from songs.models import Song

class SongAdmin(admin.ModelAdmin):
	list_display = ('song', 'title')

 #admin.site.register(Song, SongAdmin)