from django.db import models

# Create your models here.


class department(models.Model):

    Name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200, default=' ')

    def __str__(self):
        return self.Name


class employee(models.Model):
    # id=models.CharField(max_length=200)

    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to="pics", default='')
    dept = models.ForeignKey(
        department,   on_delete=models.CASCADE, default='')
    salary = models.IntegerField(default=0)
    age = models.CharField(max_length=200, default='')
    hiredate = models.DateField(default='2023-02-27')
    price = models.IntegerField(default='333')


class Student(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=15)

    class Meta:
        db_table = "student"
