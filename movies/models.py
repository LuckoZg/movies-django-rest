from django.db import models

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Organization(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Movie(models.Model):
	position = models.IntegerField()
	name = models.CharField(max_length=250)
	picture = models.CharField(max_length=500)
	score = models.IntegerField(null=True)
	description = models.TextField()
	production_company = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
	genre = models.ManyToManyField(Genre, related_name="genre")
	director = models.ManyToManyField(Person, related_name="director")
	author = models.ManyToManyField(Person, related_name="author")
	actor = models.ManyToManyField(Person, related_name="actor")

	def __str__(self):
		return self.name

class Critic(models.Model):
	text = models.TextField()
	url = models.CharField(max_length=250)
	author = models.ForeignKey(Person, on_delete=models.CASCADE)
	publisher = models.ForeignKey(Organization, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, related_name="critics")

	def __str__(self):
		return self.publisher.name + ' - ' + self.author.name