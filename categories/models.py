from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    title = models.CharField(null=False, max_length=50, unique=True)
    main_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, unique=False)

    class Meta:
        db_table = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
