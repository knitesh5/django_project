
from django import forms
 
# creating a form
class InputForm(forms.Form):
 
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField()
    
# from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email', 'job_title', 'bio')

