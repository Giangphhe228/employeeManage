from django.db import models

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=250, null=False)
    value = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'source'
        ordering = ['-id']