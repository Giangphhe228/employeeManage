from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Okr(models.Model):

    TYPE_CHOICE = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    ]

    REGULAR_TYPE_CHOICE = [
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
    ]

    STATUS_TYPE_CHOICE = [
        ('done', 'done'),
        ('fail', 'fail'),
        ('progress', 'progress'),
    ]

    objectiveId = models.IntegerField(blank=True)
    objectiveName = models.IntegerField(blank=True)
    keyResultId = models.IntegerField(blank=True)
    keyResultName = models.IntegerField(blank=True)
    title = models.CharField(max_length=250, null=False)
    formula_id= models.ForeignKey("formula.formula", related_name='formula', on_delete=models.CASCADE, null=True)
    source_id= models.ForeignKey("source.source", related_name='source', on_delete=models.CASCADE, null=True)
    type= models.CharField(max_length=50, default='0', choices=TYPE_CHOICE)
    regularly= models.CharField(max_length=50, default='daily', choices=REGULAR_TYPE_CHOICE)
    unit = models.CharField(max_length=250, null=False)
    condition = models.IntegerField()
    norm = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    result = models.IntegerField(blank=True)
    ratio = models.IntegerField(blank=True)
    note_id = models.ForeignKey("note.note", related_name='note', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default='progress', choices=STATUS_TYPE_CHOICE)
    createBy = models.CharField(max_length=250, null=False)
    updateBy = models.CharField(max_length=250, null=False)
    createAt = models.DateTimeField(null=True, blank=True)
    updateAt = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    files = ArrayField(models.CharField(max_length=100))


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Okr'
        ordering = ['-id']