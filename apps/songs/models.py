from django.db import models

# Create your models here.


class Song(models.Model):
	title = models.CharField (max_length = 100)
	artist = models.CharField (max_length = 100)
	
	GENRES = (
		("", "Please select genre"),
		("salsa" , "salsa"),
		("bachata", "bachata"),
		("kizomba", "kizomba"),

		)
	genre = models.CharField (max_length =64, choices = GENRES, default= "")
	bpm = models.PositiveSmallIntegerField(null=True,blank=True)
	music_file = models.FileField(upload_to="songs")
	
	STATS=(
		("draft","Draft"),
        ("pending","Pending"),
        ("aproved","Aproved"),
        ("rejected","Rejected"),

		)
	status = models.CharField(max_length = 32, choices = STATS, default="draft")
	price = models.PositiveSmallIntegerField(null=True,blank=True, verbose_name="Price $")