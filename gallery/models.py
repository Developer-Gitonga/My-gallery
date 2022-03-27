# from email.mime import image
# from os import name
from django.db import models


# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()


    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()   

    class Meta:
        ordering = ['first_name']   




class Category(models.Model):
    name = models.CharField(max_length=30) 

    def __str__(self):
        return self.name  


class Location(models.Model):
    location_name = models.CharField(max_length=30) 
    def __str__(self):
        return self.location_name       


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description= models.CharField(max_length=200)
    location = models.ForeignKey ('Location',on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True)
    search_fields = ['category__name']


    def save_image(self):
        self.save() 

    def __str__(self):
        return self.description


    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__name__icontains=search_term)
        return image
    
     

    
    





    

