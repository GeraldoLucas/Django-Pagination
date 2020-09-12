from django.db import models
from django.db.models import Model


class PremierLeague(Model):
    position = models.IntegerField('Position',help_text='Maximum number of 20 characters')
    club = models.CharField('Club', max_length=30, help_text='Maximum text of 30 characters')
    points = models.IntegerField('Points',help_text='Maximum numbers of 3 characters')

    def __str__(self):
        return self.club
