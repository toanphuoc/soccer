from django.conf.urls import url
from . import views
from .view import country, club

urlpatterns = [

	#----------------list url country----------
	url(r'^country/$', country.index, name='index'),
	url(r'^country/getList/$', country.get_list),
	url(r'^country/getCountry/(?P<country_id>[0-9]+)/$', country.get_country_by_id),


	#------------------list url club----------------
	url(r'^club/getList/$', club.get_list),
	url(r'^$', views.index, name='index'),
]