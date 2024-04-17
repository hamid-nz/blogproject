from django.db import models
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.




class Category(models.Model):
    name= models.CharField(max_length= 100)
    category_url= AutoSlugField(populate_from= 'name', unique= True)
    discription= models.TextField(blank=True)
    def __str__(self):
        return self.name
    
class Author(User):
   display_name= models.CharField(max_length=100, blank= True)



class BlogPost(models.Model):
    title= models.CharField(max_length=100)
    post_url= AutoSlugField(populate_from= 'title', unique= True, max_length=100)
    dicription= models.TextField(blank=True)
    featured_image= models.ImageField(upload_to='uploads')
    content=RichTextUploadingField(blank=True)
    # content=models.CharField(max_length=1000 , blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date= models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

