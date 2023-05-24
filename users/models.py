from django.db import models
from django.contrib.auth.models import User
import os
from .storage import OverwriteStorage

def image_rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user_id, ext)
    return os.path.join('profile/user/', filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    avatar = models.ImageField(default='profile/default.png', max_length=10000, storage=OverwriteStorage(), upload_to=image_rename)

    def __str__(self):
        return self.user.username
