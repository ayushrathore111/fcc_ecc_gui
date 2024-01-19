from django.db import models

# Create your models here.


class pred(models.Model):
    mod = models.IntegerField()
    out = models.IntegerField()
    fc=models.FloatField()
    tf=models.FloatField()
    ef=models.FloatField()
    ar=models.FloatField()
    ht=models.FloatField()
    area=models.FloatField()
    
    
    def __str__(self):
        return self.fc