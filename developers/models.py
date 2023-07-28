from django.db import models

from publishers.models import Publisher


# Create your models here.
class Developer(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50, null=False, unique=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Developers'

    def __str__(self):
        return self.title
