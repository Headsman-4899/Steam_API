from django.db import models


# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True)

    class Meta:
        db_table = 'Countries'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
