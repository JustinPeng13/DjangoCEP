from django.db import models
class Cat(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="pink")
    fontcolor = models.CharField(max_length=50, default="green")
    
    def __str__(self):
        return self.name

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.TextField()
    cat = models.ManyToManyField(Cat, related_name='grocery_list')
    remarks = models.TextField(blank=True)


    def __unicode__(self):
        return self.name
