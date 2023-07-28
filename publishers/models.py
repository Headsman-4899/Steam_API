from django.db import models


# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=50, null=False)
    rating = models.FloatField(null=False, default=0.0)

    class Meta:
        db_table = 'Publishers'

    def __str__(self):
        return self.name
