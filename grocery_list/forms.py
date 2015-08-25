from grocery_list.models import Item, Cat
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Button, HTML, Div, Field, Row, Fieldset
    
class ItemForm(forms.ModelForm):
    class Meta: 
        model = Item
        fields = ('name','quantity','cat','remarks','date')
        
    # helper = FormHelper()
    # helper.form_method = 'POST'
    # helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
    
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "itemform"
        
       #Create a new category multi-select list, with added css and style codes
        cat = Div('cat',css_class = "col-xs-12", style="padding:0px;") 
        oldcatselect = self.helper.layout.pop(2) #remove the original cat multi-select list
        #Insert new category multi-select list with a "Create New Category" button as a Fieldset
        self.helper.layout.insert(2, Fieldset("Select Category",cat, Button("createcatmodal", value="Create New Category", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal")))
        
        #Create a "Create New Item" button 
        self.helper.layout.append(Button('btn_createnote', 'Create Item', css_class='createnote', style="margin-top:15px;"))
        #Add a hidden field 'btn_createitem' so that it will be submitted together in the form to allow server side to 'know'
        #that this button has been clicked
        self.helper.layout.append(Hidden(name='btn_createnote', value="btn_createnote"))
        
        
    '''    
    def full_clean(self):
        #http://stackoverflow.com/questions/4340287/override-data-validation-on-one-django-form-element
        super(ItemForm, self).full_clean()
        if 'cat' in self._errors:
            self.cleaned_data['cat'] = []
            print("remove cat errors")
            del self._errors['cat']
            '''

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "catform"
        self.helper.layout.append(Hidden(name='btn_createcat', value="btn_createcat"))
        self.helper.layout.append(Button('btn_createcat', 'Create Cat', css_class='createcat', data_dismiss="modal"))


class ItemFormUpdate(forms.ModelForm):
    class Meta: 
        model = Item
        #fields = '__all__'
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super(ItemFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "itemformupdate"
        
        self.helper.add_input(Submit('submit', 'Update'))