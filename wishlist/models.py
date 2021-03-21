from django.db import models

# Create your models here.
class WishListModel(models.Model):
    title = models.CharField(max_length=20,blank=False)
    description = models.CharField(max_length=50,blank=True)
    link = models.CharField(max_length=2000,blank=True)
    image_like = models.CharField(max_length=2000,blank=True)