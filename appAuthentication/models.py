from django.db import models
from django.contrib.auth.models import User


class UserLoginModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # login time
    # logout time

    def __str__(self):
        return self.user.username

# This model will be used when the profile model is created
# class UserSignupModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # This must be added after the profile app
    # is created
