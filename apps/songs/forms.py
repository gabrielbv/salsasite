from django import forms
from songs.models import Song



class SongsForm(forms.ModelForm):
	
	
	

	class Meta:
		model=Song
		fields= ['title', 'artist', 'genre','bpm', 'music_file',"price"]
