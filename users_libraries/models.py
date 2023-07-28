from django.db import models

from games.models import Game
from users.models import User


# Create your models here.
class UserLibrary(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    total_time = models.FloatField(null=False, default=0.0)
    is_favorite = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        db_table = 'UsersLibraries'
        verbose_name_plural = 'Users libraries'

    def __str__(self):
        return str(self.id)
