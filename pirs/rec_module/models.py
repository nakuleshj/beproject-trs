from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    pics=models.ImageField(upload_to='imgs')