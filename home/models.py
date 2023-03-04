from django.db import models

# Create your models here.

#<-------- Fashion modele start------>

class TCloths(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class SCloths(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class WCloths(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
#<-------- Fashion modele End------>



#<-------- Electronices modele start------>

class Mobile(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Computer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"

class Laptop(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
#<-------- Electronices modele end------>


#<-------- Jewellery modele start------>

class Jumkas(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Necklaces(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Kangans(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='All_images')
    def __str__(self):
        return f"{self.name}   ({self.price})"

#<-------- Jewellery modele start------>