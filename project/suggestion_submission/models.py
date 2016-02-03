from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Suggestion(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(blank = True)
    description = models.TextField()

    def __str__(self):
        return self.description
