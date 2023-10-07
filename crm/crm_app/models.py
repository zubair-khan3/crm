from django.db import models

# Create your models here.
class Record(models.Model):
    created_on  = models.DateTimeField(auto_now_add=True)
    created_by  = models.CharField(max_length=50, null=True)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField(max_length=50)
    phone       = models.CharField(max_length=50)
    city        = models.CharField(max_length=50)
    address     = models.CharField(max_length=50)
    zip_code    = models.CharField(max_length=50)
     
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
        #return self.id, self.first_name