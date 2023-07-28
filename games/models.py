from django.db import models

from categories.models import Category
from developers.models import Developer
from system_requirements.models import SystemRequirement


# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    title = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField(null=False)
    cost = models.FloatField(null=False, default=0.0)
    age_rating = models.CharField(max_length=10)
    rating = models.FloatField(null=False, default=0.0)
    min_system_requirements = models.ForeignKey(SystemRequirement, on_delete=models.CASCADE, related_name='min_system_requirements')
    rec_system_requirements = models.ForeignKey(SystemRequirement, on_delete=models.CASCADE, related_name='rec_system_requirements')
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, default='', null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=False)

    class Meta:
        db_table = 'Games'

    def __str__(self):
        return self.title
