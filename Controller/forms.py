from django import forms

# creating a form
class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    name = forms.CharField()
    email = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField()
