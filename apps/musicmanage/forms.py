from django import forms
from musicmanage.models import MusicManage



class SongsForm(forms.ModelForm):
	title = forms.CharField()
	artist = forms.CharField()
	gen = forms.ChoiceField(choices=MusicManage)
	music_file = forms.FileField()

	class Meta:
		model=MusicManage
		fields= ['title', 'artist', 'gen', 'music_file']
