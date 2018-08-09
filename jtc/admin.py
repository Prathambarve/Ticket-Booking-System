from django.contrib import admin
from .models import Genre, Date, Time, Multiplex, Seats, Snumber, Star, Movies, UMovie, Role, User

# Register your models here.

admin.site.register(Genre)
admin.site.register(Date)
admin.site.register(Time)
admin.site.register(Multiplex)
admin.site.register(UMovie)
admin.site.register(Role)
admin.site.register(Star)
admin.site.register(Seats)
admin.site.register(Snumber)
admin.site.register(Movies)
admin.site.register(User)