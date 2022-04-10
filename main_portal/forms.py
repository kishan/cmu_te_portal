from django import forms
   
# creating a form 
class EmailForm(forms.Form):
    email = forms.CharField(label='Your email', max_length=100)