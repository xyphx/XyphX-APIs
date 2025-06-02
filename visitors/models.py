# models.py
from django.db import models

class Visitor(models.Model):
    total = models.IntegerField()
    portfolio = models.IntegerField()
    get_warranty = models.IntegerField()
    

    class Meta:
        managed = True  
        db_table = 'visitors'  
