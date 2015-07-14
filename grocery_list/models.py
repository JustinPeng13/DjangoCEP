from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="pink")
    fontcolor = models.CharField(max_length=50, default="green")
    
    def __unicode__(self):
        return self.name

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.TextField()
    category = models.ManyToManyField('Category', related_name='grocery_list', null=True, blank=True)
    remarks = models.TextField(blank=True)


    def __unicode__(self):
        return self.name
