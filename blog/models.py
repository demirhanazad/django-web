from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
class Categories(models.Model):
    name = models.CharField(max_length=255)
    yol= models.SlugField(null=False,blank=True, unique=True,db_index=True,editable=False)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.yol=slugify(f"{self.name}")
        super().save(*args,**kwargs)
class Hobies(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog_images")
    description = RichTextField()
    is_showed=models.BooleanField(default=False)
    yol=models.SlugField(null=False,blank=True, unique=True,db_index=True,editable=False)
    kategori=models.ForeignKey(Categories,default=1,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.yol=slugify(f"{self.title} 571610632")
        super().save(*args,**kwargs)
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='hotel_images/')