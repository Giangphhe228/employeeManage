from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.CharField(max_length=250, null=False)
    createBy = models.CharField(max_length=250, null=False)
    updateBy = models.CharField(max_length=250, null=False)
    createDate = models.DateTimeField(null=True, blank=True)
    updateDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'note'
        ordering = ['-id']