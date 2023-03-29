from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    Genders = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    gender = models.CharField(max_length=5, choices=Genders, default='M')


class Teacher(Account):
    classes = models.ManyToManyField('Class', related_name="teachers")
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Student(Account):
    student_class = models.ForeignKey('Class', on_delete=models.CASCADE, related_name="students")
    Queues = (
        ("M", 'Morning'),
        ('A', 'Afternoon'),
    )
    queue = models.CharField(max_length=9, choices=Queues)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Class(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name    

    
class Subject(models.Model):
    subject_classes = models.ManyToManyField(Class, related_name="subjects")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Homework(models.Model):
    homework_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="class_homeworks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject_homeworks")
    name = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name





    

