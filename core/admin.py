from django.contrib import admin
from .models import PremierLeague

@admin.register(PremierLeague)
class PremierLeagueAdmin(admin.ModelAdmin):
    list_display = ('position', 'club', 'points')
