from django.contrib import admin
from .models import Country, Club, Position, Player, Tournaments, Match
# Register your models here.

admin.site.register(Country)
admin.site.register(Club)
admin.site.register(Tournaments)
admin.site.register(Match)

