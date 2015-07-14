from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Item

# Create your views here.
def items_list(request):
    allitems = Item.objects.all()
    return render(request, 'grocery_list/index.html', {'items': allitems})

def item(request, item_id):
    item = Item.objects.get(id=item_id)
    resptext = ""
    resptext += "<h2>" + item.quantity + " " + item.name + "</h2>"
    resptext += "<h3> (" + item.tag + ") </h3>"
    return HttpResponse(resptext)