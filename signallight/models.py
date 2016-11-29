from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    position = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text + " " + str(self.position)
