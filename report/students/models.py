from django.db import models

# Create your models here.
class student(models.Model):
    Name=models.CharField(max_length=30)
    roll_number = models.IntegerField()
    section = models.CharField(max_length=3)
    Mark=models.IntegerField()
    grad=models.CharField(max_length=1)

    def __str__(self):
        return self.Name
    
class personlinfo(models.Model):
    #student = models.ForeignKey(student, on_delete=models.CASCADE)
    Relationship=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    Age=models.IntegerField()
