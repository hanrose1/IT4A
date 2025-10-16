from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name