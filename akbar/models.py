from django.db import models
# from django.utils import timezone

# class DumpStats(models.Model):
#     loc = models.CharField(max_length=100)
    
    
#     def __str__(self):
#         return self.loc


class DumpStats(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    full = models.BooleanField()

    def __str__(self):
        return self.name
