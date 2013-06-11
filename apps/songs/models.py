from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify

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

	def __unicode__(self):
		return self.title

####################################


# var Song_BB = Backbone.Model.extend({
#     schema: {
#         title:		'Text',
#         artist:     'Text',
#         genre:      { type: 'Select', options: ['salsa', 'bachata', 'kizomba'] },
#         bpm:		'Number',
#         # music_file: '',
#         status:      { type: 'Select', options: ['draft', 'pending', 'aproved', 'rejected'] },
#         price:      'Number'
#     }
# });

#var song_bb = new Song_BB();