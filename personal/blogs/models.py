from django.db import models

# Create your models here.
class Admin(models.Model):  
     
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    epassword = models.CharField(max_length=20)
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "Admin" 

class Blogs(models.Model):  
     
    etitle = models.CharField(max_length=100)  
    edescription = models.CharField(max_length=100) 
    edate = models.DateField(auto_now=True)
    # eimagepath = models.CharField(max_length=100)  
    class Meta:  
        db_table = "Blogs"

class Comments(models.Model):  
    ecomments = models.CharField(max_length=200)  
    ename = models.CharField(max_length=100)  
    eemail = models.CharField(max_length=100) 
    # date = models.DateField(auto_now=True)
    # eblogid = models.CharField(max_length=15)
     
    class Meta:  
        db_table = "Comments"

