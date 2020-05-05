from django.db import models

# Create your models here.

# Create a Blog model
#   title
#   pub_date
#   body
#   image
class Blog(models.Model):
    title = models.CharField(max_length=40)
    pub_date = models.CharField(max_length=10)
    body = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')

# Add the Blog app to the settings

# Create a migration

# Migrate

# Add to the admin
