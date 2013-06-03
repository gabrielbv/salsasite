from django.db import models

# Create your models here.


class MusicManage(models.Model):
	title = models.CharField (max_length = 100)
	artist = models.CharField (max_length = 100)
	gen_choice = (
		("salsa" , "salsa"),
		("bachata", "bachata"),
		("kizomba", "kizomba"),

		)
	genre = models.CharField (max_length =1, choices = gen_choice, default= "salsa")
	bpm = models.PositiveSmallIntegerField()
	music_file = models.FileField(upload_to="songs")
	status = models.CharField(max_length = 100)
	price = models.PositiveSmallIntegerField()