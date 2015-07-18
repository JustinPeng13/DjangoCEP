from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Item, Cat
import re
from django.db.models import Q

# Create your views here.
def items_list(request):
    allitems = Item.objects.all()
    total = allitems.count()
    return render(request, 'grocery_list/index.html', {'items': allitems})

def item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'grocery_list/item.html', {'item':item})

def items_cats(request, cats):
    pieces = cats.split('/') #extract different tags separated by /
    # allnotes = Note.objects.none() #required when doing normal filter pipe query ... see below
    #for p in pieces:
        #This is to combine results from different querysets from SAME model using normal pipe
        #https://groups.google.com/forum/#!topic/django-users/0i6KjzeM8OI
        #If the querysets are from different models, have to use itertools
        #http://chriskief.com/2015/01/12/combine-2-django-querysets-from-different-models/
        #allnotes = allnotes | Note.objects.filter(tag__title__iexact=p) # can have duplicates ... need another method
        
    #http://stackoverflow.com/questions/852414/how-to-dynamically-compose-an-or-query-filter-in-django
    # Turn list of values into list of Q objects
    queries = [Q(cat__title__iexact=value) for value in pieces]
    # Take one Q object from the list
    query = queries.pop()
    # Or the Q object with the ones remaining in the list
    for item in queries:
        query |= item
    print(query)
    # Query the model
    allitems = Item.objects
    total = allnotes.count();
    return render(request, 'grocery_list/index.html', {'pieces':pieces, 'items': allitems, 'total':total})   
