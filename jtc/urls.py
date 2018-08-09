from django.conf.urls import url
from . import views


urlpatterns = [

	# url(r'^(?P<logout>\D+)$', views.home1, name='home1'),
    url(r'^$', views.home, name='home'),
    url(r'^book/(?P<name>\w+)/$', views.book, name='book'),
    url(r'^termsandpolicy/$', views.terms, name='terms'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^register/$', views.register, name='register'),
    url(r'^404/$', views.error, name='error'),
    url(r'^cast/$', views.cast, name='cast'),
	url(r'^login/$', views.login, name='login'),  
	url(r'^trailer/$', views.trailer, name='trailer'),
   	url(r'^trailer/(?P<of>\w+)', views.trailer_of, name='trailer_of'),
    url(r'^booktime/$', views.booktime, name='booktime'),
    url(r'^bookdate/', views.bookdate, name='bookdate'),
    url(r'^prebook/(?P<movie>\w+)', views.prebook, name='prebook'),
    url(r'^book/(?P<name>[\w\ ]+)', views.book, name='book'),
	url(r'^booked/(?P<movie>[\w\ ]+)', views.booked, name='booked'), 
	url(r'^releases/$', views.releases, name='release'),
    

]
