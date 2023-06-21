from django.db import models

# Create your models here.
class User(models.Model):

    LEVEL_TYPE_CHOICE = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    ]

    employeeCode = models.CharField(max_length=250, null=False)
    fullName = models.CharField(max_length=250, null=False)
    gender = models.CharField(max_length=250, null=False)
    birthDate = models.CharField(max_length=250, null=False)
    phoneNumber = models.CharField(max_length=250, null=False)
    emailAddress = models.CharField(max_length=250, null=False)
    jobCode = models.CharField(max_length=250, null=False)
    jobTitle = models.CharField(max_length=250, null=False)
    officerTitle = models.CharField(max_length=250, null=False)
    locationAddress = models.CharField(max_length=250, null=False)
    organizationNamePath = models.CharField(max_length=250, null=False)
    organizationCodePath = models.CharField(max_length=250, null=False)
    createAt = models.DateTimeField(null=True, blank=True)
    updateAt = models.DateTimeField(null=True, blank=True)
    level= models.CharField(max_length=50, default='0', choices=LEVEL_TYPE_CHOICE)
    dateIn = models.DateTimeField(null=True, blank=True)
    dateOut = models.DateTimeField(null=True, blank=True)
    
    


    def __str__(self):
        return self.fullName

    class Meta:
        db_table = 'user'
        ordering = ['-id']