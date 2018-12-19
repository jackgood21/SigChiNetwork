from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    name = models.TextField()
    year = models.TextField()
    company = models.TextField()
    position = models.TextField()
    email = models.TextField()
    phone = models.TextField()



    def __str__(self):
        return self.name
