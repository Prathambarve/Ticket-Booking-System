import string, pytz, json
import datetime
from django.urls import reverse
from django.shortcuts import redirect,render, HttpResponseRedirect, get_object_or_404
from .models import *
from .forms import RegisterForm, LoginForm
from itertools import chain ## for concatenating querysets
from django.core.cache import cache

####   Provide  	menu = Movies.objects.all()[:4]  in all pages inheriting base.html for trailer list
## delete session variables after showing ticket



def home(request):
	back = Movies.objects.all()
	menu = Movies.objects.all()[:4]
	a = [0,1]
	return render(request, 'jtc/index.html', {'back':back, 'menu':menu, 'a':a})

# def home1(request, logout):
# 	back = Movies.objects.all()
# 	menu = Movies.objects.all()[:4]
# 	a = [0,1]
# 	if logout:
# 		del request.session['username']
# 	return render(request, 'jtc/index.html', {'back':back, 'menu':menu, 'a':a})
	
	
def aboutus(request):
	menu = Movies.objects.all()[:4]
	return render(request, 'jtc/aboutus.html', {'menu':menu})
	
def terms(request):
	menu = Movies.objects.all()[:4]
	return render(request, 'jtc/terms.html', {'menu':menu})


def trailer(request):
	movie = Movies.objects.all()
	menu = Movies.objects.all()[:4]
	return render(request, 'jtc/trailer.html', {'movie':movie,'menu':menu})
	
def trailer_of(request, of):
	movie = Movies.objects.all()
	add = Movies.objects.filter(title = of)
	menu = Movies.objects.all()[:4]
	return render(request, 'jtc/trailer.html', {'movie':movie,'menu':menu,'add':add})

	
def releases(request):
	movie = Movies.objects.all().order_by('-release')
	menu = Movies.objects.all()[:4]
	return render(request, 'jtc/release.html', {'movie':movie, 'menu':menu})


def cast(request):
	menu = Movies.objects.all()[:4]
	stars = Star.objects.all()
	return render(request, 'jtc/cast.html', {'stars':stars, 'menu':menu})

def gallery(request):
	menu = Movies.objects.all()[:4]
	movies = Movies.objects.all()
	return render(request, 'jtc/gallery.html', {'menu':menu, 'movies':movies})
	

def error(request):
	menu = Movies.objects.all()[:4]
	back = Movies.objects.all()
	return render(request, 'jtc/404.html', {'menu':menu, 'back':back})


def register(request):
	menu = Movies.objects.all()
	back = Movies.objects.all()
	# if request.has_key('username'): # #  REMOVE if not using cookies for sessions 
		# return render(request, 'jtc/login')
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			user_fname = form.cleaned_data['fname']
			user_lname = form.cleaned_data['lname']
			user_password = form.cleaned_data['password']
			try:
				user = get_object_or_404(User, email = user_email)
				a = "%s is already associated with us. Try Logging in "% (user_email)
				return render(request, 'jtc/register.html', {'a':a, 'menu':menu, 'form':form})
			except:
				usr = User()
				usr.fname = user_fname
				usr.lname = user_lname
				usr.email = user_email
				usr.password = user_password
				usr.save()
				return render(request, 'jtc/index.html', {'back':back, 'menu':menu})
	else:
		form = RegisterForm()
		return render(request, 'jtc/register.html', {'menu':menu, 'form':form})
		
def login(request):
	back = Movies.objects.all()
	menu = Movies.objects.all()[:4]
	if request.session.has_key('username'):
		return render(request, 'jtc/index.html', {'menu':menu, 'back':back})
	else:
		username = 'Not Logged In'
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				user_email = form.cleaned_data['email']
				user_password = form.cleaned_data['password']
				try:
					print(user_email)
					user = User.objects.get(email = user_email)
					if user.password == user_password:
						request.session['username']=user.fname+ user.lname 
						return HttpResponseRedirect(reverse('home', {'menu':menu, 'back':back}))
					else:
						a = "Incorrect password " 
						return render(request, 'jtc/login.html', {'form':form, 'menu':menu, 'a':a })
				except:
					a = "%s is not associated with us kindly Signup first " %(user_email)
					return render(request, 'jtc/login.html', {'form':form, 'menu':menu, 'a':a })
		else:
			form= LoginForm()
		return render(request, 'jtc/login.html', {'menu':menu, 'form':form})
	

def bookdate(request):
	if request.is_ajax():
		mov = request.POST.get('mov')
		multiplex = request.POST.get('multiplex')
		print (mov+"   "+multiplex)
		movie = Movies.objects.get(title = mov)
		for mult in movie.multiplexes.all():
			try:
				if mult.name == multiplex:
					date = mult.date.all()
					request.session['mul_id']=mult.pk
					return render(request, 'jtc/bookdate.html', {'dates':date})
			except:
				pass
	return render(request, 'jtc/bookdate.html',{})

def booktime(request):
	if request.is_ajax():
		mov = request.POST.get('mov')
		multiplex = request.POST.get('multiplex')
		date = str(request.POST.get('date'))
		movie = Movies.objects.get(title = mov)
		for mult in movie.multiplexes.all():
			try:
				if mult.name==multiplex:
					taarikh = mult.date.all()
					for dat in taarikh:
						a = str(dat)
						if a == date:
							time = mult.time.all()
							request.session['date_id']=dat.pk
							return render(request, 'jtc/booktime.html', {'times':time})
			except:
				pass
	return render(request, 'jtc/booktime.html', {})

def prebook(request, movie):
	menu = Movies.objects.all()[:4]
	film = get_object_or_404(Movies, title__icontains = movie)
	return render(request, 'jtc/prebook.html', {'menu': menu, 'film':film})




def book(request, name):
	if request.method=='POST':
		request.session['date']=request.POST.get('date')
		request.session['time']=request.POST.get('time')
		request.session['multiplex']=request.POST.get('multiplex')
		t = request.POST.get('time')
		time = Time.objects.get(timing = t)
		time_id = time.pk
		try:
			movie = get_object_or_404(Movies, title = name)
			a = [x for x in range(1,19)] # For seat rows
		except:
			a = []
			return render(request, 'jtc/book.html', {'a':a})

		return render(request, 'jtc/book.html', {'movie':movie, 'a':a, 't':time_id})


def booked(request, movie):
	menu = Movies.objects.all()[:4]
	alpha = list(string.ascii_uppercase)
	if request.method == 'POST':
		time1 = request.session.get('time')
		del request.session['time']
		date1 = request.session.get('date')
		del request.session['date']
		mul = request.session.get('multiplex').split('-')
		mulplx = str(mul[0])
		location = str(mul[1])
		print(mulplx)
		print(location)
		mov = get_object_or_404(Movies, title = movie)
		print (mov.banner)
		multiplex = get_object_or_404(Multiplex, name = mulplx, location = location)
		time = Time.objects.get(timing = time1)
		date = Date.objects.get(date = date1)
		p = request.POST.dict()
		seats=True
		for alph in alpha:
			if alph == 'R':
				break
			else:
				for i in range(1,19):
					a = alph + str(i)
					try:
						se = p[a]
						if se == 'False' or se == 'false':
							seats = False
						elif se == 'true' or se == 'True':
							seats = True							
					except:
						continue
					if seats == False:
						try:
							addseat = Snumber.objects.get(seat_name = a, seat_avail = seats)
							removeseat = Snumber.objects.get(seat_name = a, seat_avail = True)
							seat = Seats.objects.get(movie_name = mov, multiplex_name = multiplex, date=date, time=time)
							for st in seat.seat_no.all():
								if removeseat == st:
									seat.seat_no.remove(removeseat)
								seat.seat_no.add(addseat)
						except:
							pass
				seat = Seats.objects.get(movie_name = mov, multiplex_name = multiplex, date = date, time = time)
	else:
		HttpResponseRedirect(reverse('home'))
		
	return HttpResponseRedirect(reverse('home'))

