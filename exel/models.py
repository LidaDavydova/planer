from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

class Fileexel(models.Model):
    date = models.DateTimeField(default=timezone.now)
    cover = models.FileField(upload_to='media/')
    


    
class Customer(models.Model):
    #user_name = models.CharField(max_length = 100)
    
    first_name = models.CharField(max_length = 50)

    last_name = models.CharField(max_length = 50)

    password = models.CharField(max_length = 50)
    
    
    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)
    
class Brief(models.Model):
    
    sum_all = models.IntegerField()
    
    landing_page = models.TextField()
    
    description = models.TextField()
    
    UTP = models.TextField()
    
    competitors = models.TextField()
    
    terms = models.TextField()
    
    geography = models.TextField()
    
    KPI = models.TextField()
    
    audience = models.TextField()
    
    suggestions = models.TextField()
    
    companies_before = models.TextField()
    
    who_prep_materials = models.TextField()
    
    instrument = models.TextField()
    
    official_list = models.TextField()
    
    CRM = models.TextField()
    
    def __str__(self):
        return self