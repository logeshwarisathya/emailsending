from django.db import models

# Create your models here.

class Marks(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(null=True)
    tamil=models.PositiveIntegerField()
    english=models.PositiveIntegerField()
    maths=models.PositiveIntegerField()
    science=models.PositiveIntegerField()
    social=models.PositiveIntegerField()