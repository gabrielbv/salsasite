from django.contrib import admin

from songs.models import Song

class SongAdmin(admin.ModelAdmin):
	list_display = ('artist', 'title')

admin.site.register(Song, SongAdmin)