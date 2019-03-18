from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    class that contains user Profile properties
    '''
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField()
    contact = models.IntegerField(blank=True, null=True,)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.bio

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(save_user_profile, sender=User)

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()
