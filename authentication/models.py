from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # name = models.CharField(max_length=100, null=True)
    email   = models.EmailField('email address', unique=True, null=True)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.user.username
    #
    # def create_user_callback(sender, instance, **kwargs):
    #     UserProfile. new = UserProfile.objects.get_or_create(user=instance)
    # post_save.connect(create_user_callback, User)
