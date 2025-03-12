from django.db import models

class main(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
