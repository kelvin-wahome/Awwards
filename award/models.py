from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  '''
  class that contains user Profile properties
  '''
  profile_pic = models.ImageField(upload_to='images/',null=True, blank=True)
  bio = models.TextField()
  contact = models.IntegerField(blank=True, null=True,)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
