from django import forms
from phonenumber_field.formfields import PhoneNumberField


class SearchForm(forms.Form):
    email = forms.EmailField()
    phone = PhoneNumberField(region="RU")
    date = forms.DateField()
    text = forms.CharField(required=False)
