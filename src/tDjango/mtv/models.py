'''
Created on 2012-8-15

@author: dell
'''
from django.db import models
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    website=models.URLField()
    def __unicode__(self):
        return self.name
    @classmethod
    def create(cls,name,addr):
        pub=cls(name=name,address=addr)
        return pub
        
    
    
    
class Author(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher);
    date=models.DateField()                              