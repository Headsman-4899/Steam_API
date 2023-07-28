from django.db import models


# Create your models here.
class SystemRequirement(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    os = models.CharField(null=False, max_length=20)
    processor = models.CharField(null=False, max_length=50)
    ram = models.IntegerField(null=False, default=8)
    video_card = models.CharField(null=False, max_length=50)
    direct_x = models.CharField(null=False, max_length=50)
    disk_space = models.IntegerField(null=False)

    class Meta:
        db_table = 'SystemRequirements'

    def __str__(self):
        return self.os + " " + self.processor + " " + self.video_card
