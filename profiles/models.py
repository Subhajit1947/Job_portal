from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User=get_user_model()

class Profile(models.Model):
    class Role(models.TextChoices):
        poster='POSTER',_('Poster')
        seeker='SEEKER',_('Seeker')
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='Profile')
    role=models.CharField(choices=Role.choices,default=Role.seeker)
   