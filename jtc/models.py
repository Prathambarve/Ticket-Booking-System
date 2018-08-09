from django.db import models

# Create your models here.
class Genre(models.Model):
	genre_name = models.CharField(max_length= 20, unique=True)
	
	def __str__(self):
		return self.genre_name
	class Meta:
		verbose_name_plural="Genres"
		


class Time(models.Model):
	timing = models.TimeField(default="09:50:00")
	
	def __str__(self):
		return "%s" %(self.timing)
	class Meta:
		ordering = ['timing']


	
class Date(models.Model):
	date = models.DateField(default="2017-04-19")
	
	def __str__(self):
		a = "%s"%(self.date)
		return a
		
	
	
class Multiplex(models.Model):
	name = models.CharField(max_length=60)
	location = models.CharField(max_length=200)
	seats_avail = models.BooleanField(default = True)
	date = models.ManyToManyField(Date)
	time = models.ManyToManyField(Time)
	movie = models.CharField(max_length=30, default='movie')
	
	def __str__(self):
		return self.name + ' '+self.location+' '+self.movie
	class Meta:
		verbose_name_plural="multiplexes"
		ordering = ['movie']
		
# # contains only name of upcoming movie nothing else
class UMovie(models.Model):
	name = models.CharField(max_length= 200, unique=True)
	
	def __str__(self):
		return self.name

 # #  This class contains name of role played in movie by star
class Role(models.Model):
	name = models.CharField(max_length=30, unique=True)
	movie = models.CharField(max_length= 100, default="movie_name")
	
	def __str__(self):
		return self.name
	
# # contains name of star and all info 
class Star(models.Model):
	name = models.CharField(max_length=30, unique=True)
	image = models.CharField(max_length=100, default="/static/jtc/img/name.jpg")
	gender = models.CharField(max_length=7, default="Actor")
	roles = models.ManyToManyField(Role)
	upcoming_movies = models.ManyToManyField(UMovie)
	about = models.TextField(default="A very talented acter")
	
	def __str__(self):
		return self.name

# # Contain name of movie and all info of movie 	
class Movies(models.Model):
	title = models.CharField(max_length=60)
	release = models.DateField()
	banner = models.CharField(max_length= 200, default="/static/jtc/img/name.jpg")
	menu_poster = models.CharField(max_length= 200, default="/static/jtc/img/name.jpg")
	poster = models.CharField(max_length= 200, default="/static/jtc/img/name.jpg")
	page_link = models.TextField(blank=True, null=True)
	trailer_link = models.TextField()
	rating = models.SmallIntegerField()
	story_line = models.TextField()
	genre = models.ManyToManyField(Genre)    ## Get genre of a movie by query #object#.genre.all()
	multiplexes = models.ManyToManyField(Multiplex)
	stars = models.ManyToManyField(Star)
	
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural="movies"

		
class Snumber(models.Model):
	seat_avail = models.BooleanField(default=True)
	seat_name = models.CharField(max_length=4)
	
	def __str__(self):
		return self.seat_name + str(self.seat_avail)
	
	class Meta:
		unique_together = ('seat_avail','seat_name')
		ordering=['id']


class Seats(models.Model):
	seat_no = models.ManyToManyField(Snumber)
	movie_name = models.ForeignKey(Movies)
	multiplex_name = models.ForeignKey(Multiplex)
	date = models.ForeignKey(Date)
	time = models.ForeignKey(Time)
	
	def __str__(self):
		b = str(self.date)
		c = str(self.time)
		d = str(self.multiplex_name)
		return d+" "+b+" "+c



	class Meta:
		unique_together = ('movie_name', 'multiplex_name', 'date', 'time')
		verbose_name_plural="Seats"	


# # Now Database for User login and registrations
class User(models.Model):
	fname = models.CharField(max_length= 15, default="fname")
	lname = models.CharField(max_length= 15, default="lname")
	email = models.EmailField(max_length= 254, unique=True)
	password = models.CharField(max_length= 40)
	
	def __str__(self):
		return (self.fname+self.lname)