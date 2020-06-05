from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
     on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users', blank=True,
     verbose_name='Аватар')

    def __str__(self):
        return 'Профиль пльзователя {}'.format(self.user.username)
