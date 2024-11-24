from django.db import models

# Create your models here.
class BookTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name

class ContactTable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')  # Field to upload images to 'images/' directory
    title = models.CharField(max_length=50)  # Field for the image title
    price = models.CharField(max_length=50)  # Field for the price (stored as text)

    def __str__(self):
        return self.title  # Display the title as the string representation

class Member(models.Model):
    name = models.CharField(max_length=100)  # Full name of the member.
    username = models.CharField(max_length=100)  # Username for the member.
    password = models.CharField(max_length=64)  # Password, typically hashed.

    def __str__(self):
        return self.name  # Returns the name of the member when the object is printed.