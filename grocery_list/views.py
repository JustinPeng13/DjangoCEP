from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Item, Cat
from accounts.models import UserProfile
import re
from django.db.models import Q
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ItemForm, CatForm, ItemFormUpdate
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
# Create your views here.
def items_list(request):
    allitems = Item.objects.all()
    total = allitems.count()
    return render(request, 'grocery_list/index.html', {'items': allitems, 'total': total})
    
class ItemList(ListView):
    model = Item
    allitems = Item.objects.all()
    total = 10
    
    def get_queryset(self):
        cat = self.kwargs['cat']
        if cat == '':
            return Item.objects.all()
        else:
            return Item.objects.filter(cat__name__iexact=cat)
        

def item(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'grocery_list/item.html', {'item':item})

def items_cats(request, cats):
    pieces = cats.split('/') #extract different cats separated by /
    # allnotes = Note.objects.none() #required when doing normal filter pipe query ... see below
    #for p in pieces:
        #This is to combine results from different querysets from SAME model using normal pipe
        #https://groups.google.com/forum/#!topic/django-users/0i6KjzeM8OI
        #If the querysets are from different models, have to use itertools
        #http://chriskief.com/2015/01/12/combine-2-django-querysets-from-different-models/
        #allnotes = allnotes | Note.objects.filter(cat__title__iexact=p) # can have duplicates ... need another method
        
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
    total = allitems.count();
    return render(request, 'grocery_list/index.html', {'pieces':pieces, 'items':allitems, 'total':total})   

class ItemCreate(CreateView):
    model = Item
    form_class = ItemForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemCreate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ItemCreate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemFormUpdate
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ItemUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('items_list',kwargs={"cat":""})
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemDelete, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ItemDelete, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

    
class MyView(TemplateView):
    #setup the various forms in this view
    cat_form_class = CatForm
    item_form_class = ItemForm
    template_name = "grocery_list/item_hybrid.html"

    #called when loading the page for a new entry
    def get(self, request, *args, **kwargs):
        #setup all the forms by intialising the various form names with the corresponding form class
        kwargs.setdefault("createcat_form", self.cat_form_class())
        kwargs.setdefault("createitem_form", self.item_form_class())
        #Added curruser so that profile picture of curruser can be rendered.
        kwargs.setdefault('curruser', UserProfile.objects.get(user=self.request.user))
        return super(MyView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        
        #if btn_createcat hidden field is a value in POST form
        if "btn_createcat" in request.POST['form']: 
            form = self.cat_form_class(**form_args)
            if not form.is_valid():
                #Construct the failed status (0) and the errors as message to be displayed in the template
                response_dict = {}
                response_dict['status'] = 0
                response_dict['message'] = form.errors.as_ul()
                return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))
                #return self.get(request, createcat_form=form)
            else:
                #form is valid, save the form, and return all folders as data to update the category multi-select list
                form.save() #save the new object
                data = Cat.objects.all() # retrieve all records
                response_dict = {'status': 1}
                response_dict['message'] = list(data.values('id','name'))
                return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
        #if btn_createnote hidden field is a value in POST form
        elif "btn_createnote" in request.POST['form']:
            form = self.item_form_class(**form_args)
            if not form.is_valid():
                #Construct the failed status (0) and the errors as message to be displayed in the template
                response_dict = {}
                response_dict['status'] = 0
                response_dict['message'] = form.errors.as_ul()
                return HttpResponse(json.dumps(response_dict, cls=DjangoJSONEncoder))
                #return self.get(request, createitem_form=form, errors=response_dict) 
            else:
                try:
                    #Find out which user is logged in and get the correct UserProfile record.
                    curruser = UserProfile.objects.get(user=self.request.user)
                    print("hhh", self.request.POST['cat'])
                    obj = form.save(commit=False)
                    obj.user = curruser #Save the note note under that user
                    obj.save() #save the new object
                    
                except Exception, e:
                    print("errors" + str(e))
                response = {'status': 1, 'message':'ok'}
                return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
            
        return super(MyView, self).get(request)
        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
    
    def get_queryset(self):
        #self.request.user will contain the "User" object, however,
        #user field in the Item model is an instance of "UserProfile" object
        #So need to ensure that when we filter all the user owned items, we
        #filter using the 'correct' UserProfile instance based on logged in "User" object 
        #in self.request.user
        curruser = UserProfile.objects.get(user=self.request.user)
        cat = self.kwargs['cat']
        if cat == '':
            #filter based on current logged in user
            self.queryset = Item.objects.filter(user=curruser)
            return self.queryset
        else:
            #filter based on current logged in user
            self.queryset = Item.objects.all().filter(user=curruser).filter(folder__title__iexact=cat)
            return self.queryset