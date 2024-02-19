from django.db import models
from django.core.validators import MinLengthValidator , RegexValidator
from rest_framework import serializers

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120 , validators=[MinLengthValidator(10 , message="mobile number must be at least 10 digit numbers ."),RegexValidator(r'^9\d{9}$' , message='mobile number must be at least 9 digit and 10 digit long')])
    date = models.DateField()
    image = models.ImageField(upload_to='employee_images/')
    
    def __str__(self):
        return self.name
    
class EmployeeSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
