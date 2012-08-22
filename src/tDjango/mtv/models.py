# _*_ coding: utf-8 _*_
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    website = models.URLField()
    def __unicode__(self):
        return self.name
    @classmethod
    def create(cls, name, addr):
        pub = cls(name=name, address=addr)
        return pub
        
    
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    @classmethod
    def authorInstance(cls, fname, lname, email):
        a = cls(first_name=fname, last_name=lname, email=email)
        return a
    def __unicode__(self):
        return self.first_name
    
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher);
    date = models.DateField()     
    @classmethod
    def bookInstance(cls, title, publisher, date):
        b = cls(title=title,  publisher=publisher, date=date)
        return b  
    def __unicode__(self):
        return self.title
    #严格按照四个空格
    class Meta:
        ordering=['-date']
    
    
    
class Person(models.Model):
    #2tuples
   SHIRT_SIZES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
    ) 
   name = models.CharField(max_length=20, unique=True)
   shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
   @classmethod
   def personInstance(cls, name, shirt_size):
       p = cls(name=name, shirt_size=shirt_size)
       return p
       
                         
