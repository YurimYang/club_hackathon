from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=45)  

class Club(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, db_column= "user_id")
    title = models.CharField(max_length=60)
    activity = models.IntegerField()
    clubfield=models.IntegerField()
    leader = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length= 45)
    body = models.CharField(max_length=1000)
    

class Matching(models.Model):
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE, db_column="club_id")
    match_date = models.DateTimeField()
    match_body = models.CharField(max_length=1000)

class Field(models.Model):
    fieldname = models.CharField(max_length=20)
    def __str__(self):
        return self.fieldname

class midField(models.Model):
    fieldnameId = models.ForeignKey(Field, on_delete=models.CASCADE, db_column="fieldnameId")
    midfieldname = models.CharField(max_length=20)
    def __str__(self):
        return self.midfieldname

class lastField(models.Model):
    fieldnameId = models.ForeignKey(Field, on_delete=models.CASCADE, db_column="fieldnameId")
    midfieldnameId = models.ForeignKey(midField, on_delete=models.CASCADE, db_column="midfieldnameId")
    lastfieldname = models.CharField(max_length=20)
    def __str__(self):
        return self. lastfieldname