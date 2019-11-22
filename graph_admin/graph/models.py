from django.db import models

# Create your models here.

class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField()
    status = models.BooleanField(default=True,null=True)
    date_add = models.DateTimeField(auto_now_add=True,null=True)
    date_udp = models.DateTimeField(auto_now=True,null=True)
    


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    status = models.BooleanField(default=True,null=True)
    date_add = models.DateTimeField(auto_now_add=True,null=True)
    date_udp = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    status = models.BooleanField(default=True,null=True)
    date_add = models.DateTimeField(auto_now_add=True,null=True)
    date_udp = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,related_name='publisher')
    status = models.BooleanField(default=True,null=True)
    date_add = models.DateTimeField(auto_now_add=True,null=True)
    date_udp = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    status = models.BooleanField(default=True,null=True)
    date_add = models.DateTimeField(auto_now_add=True,null=True)
    date_udp = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name