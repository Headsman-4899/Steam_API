from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from countries.models import Country
# admin: admin


# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    balance = models.FloatField(default=0.0)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(default=timezone.now())
    is_active = models.BooleanField(default=True)
    is_invisible = models.BooleanField(default=False)
    last_time_online = models.DateTimeField(default=timezone.now())
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.username
