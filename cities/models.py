from django.db import models

from countries.models import Country


# Create your models here.
class City(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cities'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
