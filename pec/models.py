from django.db import models



class Server(models.Model):
    profession=models.CharField(max_length=100)
    image=models.FileField(null=True,blank=True)

    about=models.TextField()

    def __str__(self):
        return self.profession
    def get_absolute_url(self):
        return "/%s/" %(self.id)


class Carpenter(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(null=True,blank=True)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    lat=models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)
    dist=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "collab/services/clist"

    class Meta:
        ordering=["dist"]


class Driver(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(null=True,blank=True)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    lat=models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)
    dist=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=["dist"]


class Plumber(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(null=True,blank=True)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    lat=models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)
    dist=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=["dist"]



class Mason(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(null=True,blank=True)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    lat=models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)
    dist=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=["dist"]



class User(models.Model):
    address=models.TextField()
    lat=models.FloatField(null=True,blank=True)
    long=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.name
