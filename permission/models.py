from django.db import models

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=250, null=False)
    createBy = models.CharField(max_length=250, null=False)
    updateBy = models.CharField(max_length=250, null=False)
    createAt = models.DateTimeField(null=True, blank=True)
    updateAt = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'permission'
        ordering = ['-id']