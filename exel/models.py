from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone



class Customer(models.Model):
    #user_name = models.CharField(max_length = 100)
    
    first_name = models.CharField(max_length = 50)

    last_name = models.CharField(max_length = 50)

    password = models.CharField(max_length = 50)
    
    
    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)
    
class Specification(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name='Имя хар-к')
    
    def __str__(self):
        return 'Хар-ки {}'.format(self.name)