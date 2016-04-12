from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .view import country, club

urlpatterns = [

	#----------------list url country----------
	url(r'^country/$', country.index, name='index'),
	url(r'^country/getList/$', country.get_list),
	url(r'^country/getCountry/(?P<country_id>[0-9]+)/$', country.get_country_by_id),
	url(r'^country/create/$', country.create),
	url(r'^country/update/(?P<country_id>[0-9]+)/$', country.update),
	# url(r'^country/delete/(?P<country_id>[0-9]+)/$', country.delete),

	#------------------list url club----------------
	url(r'^club/getList/$', club.get_list),
	url(r'^$', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)