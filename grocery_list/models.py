from django.db import models
from django.core.urlresolvers import reverse

class Cat(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, default="pink")
    fontcolor = models.CharField(max_length=50, default="green")
    
    def __str__(self):
        return self.name

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cat = models.ManyToManyField(Cat, related_name='grocery_list', blank=True)
    remarks = models.TextField(blank=True)
    date = models.DateField(blank=True)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})

    def __unicode__(self):
        return self.name
