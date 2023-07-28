from games.models import Game
from users.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Review(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    comment = models.CharField(max_length=255, null=False, default='')
    point = models.FloatField(null=False, default=0.0)
    created_date = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, unique=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True, unique=False)

    class Meta:
        db_table = 'Reviews'

    def __str__(self):
        return self.comment
