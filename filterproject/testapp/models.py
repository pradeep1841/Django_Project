from django.db import models

class FilterModel(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    date=models.DateField()
    
