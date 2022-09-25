
from django import forms
from django.forms import HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
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
        fields = ('emp_id','name', 'email', 'job_title', 'bio','file')



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UploadFileForm(forms.Form):
	file = forms.FileField()
