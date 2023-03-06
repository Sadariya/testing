from django.db import models
from datetime import datetime

# Create your models here.

class chairmans_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class events_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    event_name =models.CharField(max_length=100)
    event_time = models.DateField(default=datetime.now(),blank=True)
    event_img = models.FileField(upload_to='static/upload',blank=True)
    event_information = models.TextField(blank=True)
    comments = models.TextField(blank=True)

class notices_view_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class notices_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class transactions_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class user_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class visitors_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class watchmans_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

    
class signup_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    mail = models.EmailField()

class members_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.EmailField(max_length=50)
    password = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    Mobile = models.BigIntegerField()
