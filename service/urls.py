from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .view import country, club, tournaments

urlpatterns = [

	#----------------list url country----------
	url(r'^country/$', country.index, name='index'),
	url(r'^country/get_list/$', country.get_list),
	url(r'^country/get_country/(?P<country_id>[0-9]+)/$', country.get_country_by_id),
	url(r'^country/create/$', country.create),
	url(r'^country/update/(?P<country_id>[0-9]+)/$', country.update),
	url(r'^country/delete/(?P<country_id>[0-9]+)/$', country.delete),

	#------------------list url club----------------
	url(r'^$', views.index, name='index'),
	url(r'^club/get_list/$', club.get_list),
	url(r'^club/get_club/(?P<club_id>[0-9]+)/$', club.get_club_by_id),
	url(r'^club/create/$', club.create),

	url(r'^tournaments/$', tournaments.index, name='index'),
	url(r'^tournaments/get_list/$', tournaments.get_list),
	url(r'^tournaments/create/$', tournaments.create),
	url(r'^tournaments/get_all_tournaments_in_country/(?P<country_id>[0-9]+)/$', tournaments.get_all_tournaments_in_country),
]

urlpatterns = format_suffix_patterns(urlpatterns)