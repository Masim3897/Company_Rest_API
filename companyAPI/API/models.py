from django.db import models

# Create your models here.
class company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length = 100,
                            choices = (
                                ('it','it'),
                                ('non it','non it'),
                                ('phones','phones')
                            ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    name = models.CharField(max_length =50)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length = 20)
    about = models.TextField()
    positions = models.CharField(max_length = 100,
                            choices = (
                                ('manager','manager'),
                                ('developer','developer'),
                                ('testing engineer','te')
                            ))
    cmpany = models.ForeignKey(company,on_delete=models.CASCADE)    
    