from jtc.models import *
mul_name = ['Silver', 'PVR']

for i in mul_name:
	j = str(i)
	m = Movies.objects.get(title__icontains = "laali")
	mul = Multiplex.objects.get(movie__icontains = 'laali', name__icontains= j)
	date = mul.date.all()
	time = mul.time.all()
	seatt = Snumber.objects.filter(seat_avail = True)
	
	Seats.objects.bulk_create([
		Seats(movie_name=m, multiplex_name=mul, date=dt, time=tm) for dt in date for tm in time
		])
	
	
	seat = Seats.objects.filter(movie_name=m, multiplex_name=mul)
	
	for st in seat:
		for stt in seatt:
			st.seat_no.add(stt)
