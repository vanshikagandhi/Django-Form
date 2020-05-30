from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    COMPANY_NAME=models.CharField(max_length=100)
    FRONT_INSIDE_PICTURE = models.FileField(upload_to='profile_pics', blank=True)
    BUSINESS_CARD_IMAGE=models.FileField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.COMPANY_NAME

