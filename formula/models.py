from django.db import models

# Create your models here.
class Formula(models.Model):
    name = models.CharField(max_length=250, null=False)
    value = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'formula'
        ordering = ['-id']