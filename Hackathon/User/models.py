from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, db_column="user")
    # username = models.CharField(max_length = 45) #사용자 id
    # password = models.CharField(max_length = 45) #사용자 pw
    name = models.CharField(max_length = 15) #사용자 성함 
    leader = models.IntegerField() #0이면 리더x 1이면 리더 


