from django import forms

class PersonForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    contact_address = forms.CharField(max_length=50)