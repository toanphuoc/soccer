from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .view import country, club, tournaments, match, video_type, match_detail

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

	#--------------------list url tournaments------------------------------
	url(r'^tournaments/$', tournaments.index, name='index'),
	url(r'^tournaments/get_list/$', tournaments.get_list),
	url(r'^tournaments/create/$', tournaments.create),
	url(r'^tournaments/get_all_tournaments_in_country/(?P<country_id>[0-9]+)/$', tournaments.get_all_tournaments_in_country),

	#--------------------list url video type-------------------------------------
	url(r'^video_type/$', video_type.index, name='index'),
	url(r'^video_type/get_list/$', video_type.get_list),

	#--------------------list url about match-----------------------------------
	url(r'^match/$', match.index, name='index'),
	url(r'^match/create/$', match.create),
	url(r'^match/get_list/$', match.get_list),
	url(r'^match/get_list_today/$', match.get_match_today),
	url(r'^match/get_match_by_tournament/(?P<tournament_id>[0-9]+)/$', match.get_match_by_tournament),

	#-------------------------list url match detail-----------------------------------
	url(r'^match_detail/$', match_detail.index, name='index'),
	url(r'^match_detail/create/$', match_detail.create),
	url(r'^match_detail/get_video_of_match/(?P<match_id>[0-9]+)/$', match_detail.get_video_match),

]

urlpatterns = format_suffix_patterns(urlpatterns)