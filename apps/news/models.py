from django.db import models
from django.contrib.auth.models import User




class News(models.Model):  

	user = models.ForeignKey(User)
	
	title = models.CharField(max_length=50)
	content = models.TextField()
	published = models.DateField()
	
	APPROVED="APPROVED"
	PENDING ="PENDING"
	DRAFT = "DRAFT"

	STATS= (

		(APPROVED, "Approved"),
		(PENDING, "Pending"),
		(DRAFT, "Draft"),

	)

	status=models.CharField(   max_length=20,
							   choices = STATS,
							   default=DRAFT)


	class Meta:

		verbose_name_plural = "News"

	def __unicode__(self):
		return self.title