from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_desc=models.CharField(max_length=20)

    def __str__(self):
     return str(self.dep_name)

class Student(models.Model):
   Student_name=models.CharField(max_length=20)
   email=models.EmailField()
   city=models.CharField(max_length=40)
   Dep_no=models.ForeignKey(Department,on_delete=models.CASCADE)
   def __str__(self):
      return self.Student_name