from django.db import models
from django.utils import timezone

from games.models import Game
from users.models import User


# Create your models here.
class UserDesiredGames(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    added_date = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        db_table = 'UserDesiredGames'

    def __str__(self):
        return str(self.id)
    