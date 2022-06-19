from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)


class Branch(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=60)



class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    facebook = models.CharField(max_length=150)


class Course:
    name = models.CharField(max_length=60)
    description = models.TextField()
    category = models.CharField(max_length=20)
    logo = models.ImageField()
    contacts = models.IntegerField()
    branches = models.CharField(max_length=100)


