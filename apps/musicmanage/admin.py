from django.contrib import admin

from musicmanage.models import MusicManage

class UserMusicManage(admin.ModelAdmin):
	list_display = ('song', 'title')

#admin.site.register(MusicManage, UserMusicManage)