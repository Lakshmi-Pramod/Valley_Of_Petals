from django.db import models

# Create your models here.
class flora(models.Model):
    flora_id=models.CharField(max_length=120)
    species=models.CharField(max_length=120)
    region=models.CharField(max_length=120)
    evaluated_date=models.DateField()

class habitat(models.Model):
    climate=models.CharField(max_length=120)
    altitude_range=models.CharField(max_length=120)
    season=models.CharField(max_length=120)
    soil=models.CharField(max_length=120)
    flora_id=models.CharField(max_length=120)

class characteristics(models.Model):
    b_name=models.CharField(max_length=100)
    utility=models.CharField(max_length=120)
    avail=models.CharField(max_length=120)
    flora_id=models.CharField(max_length=120)

class marketValue(models.Model):
    item_id=models.CharField(max_length=50)
    flora_id=models.CharField(max_length=120)
    cons=models.CharField(max_length=120)
    exp=models.FloatField()
    cost=models.FloatField()

class Notification(models.Model):
    n_id=models.CharField(max_length=50)
    flora_s=models.CharField(max_length=100)
    login_date=models.DateField()
    t_in=models.TimeField()
    t_out=models.TimeField()
    v_id=models.CharField(max_length=100)

class Viewer(models.Model):
    v_id=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    psd=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin=models.IntegerField()

class viewer_email(models.Model):
    v_id=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    
class can_view(models.Model):
    flora_id=models.CharField(max_length=100)
    v_id=models.CharField(max_length=100)



