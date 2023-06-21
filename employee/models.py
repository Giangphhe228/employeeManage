from django.db import models

# Create your models here.
class Employee(models.Model):
    
    POSITION_TYPE_CHOICE = [
        ('employee', 'employee'),
        ('CBQL', 'CBQL'),
        ('TL', 'TL'),
    ]
    department = models.ForeignKey('department.department', related_name='employee_department', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250, null=False)
    position= models.CharField(max_length=50, default='employee', choices=POSITION_TYPE_CHOICE)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'
        ordering = ['-id']