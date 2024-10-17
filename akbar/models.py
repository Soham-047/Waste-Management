from django.db import models
from django.utils import timezone

class DumpStats(models.Model):
    loc = models.CharField(max_length=100)
    full = models.BooleanField()
    
    def __str__(self):
        return self.loc
