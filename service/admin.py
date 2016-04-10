from django.contrib import admin
from .models import Country, Club, Position, Player
# Register your models here.

admin.site.register(Country)
admin.site.register(Club)
admin.site.register(Position)
admin.site.register(Player)

