from django.db import models


class Thing(models.Model):
    related_thing = models.ForeignKey('Thing', null=True, blank=True)
    name = models.CharField(max_length=255, help_text='The name of the thing')
