from django import forms

class retiroForm(forms.Form):
    code = forms.CharField(max_length=15)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    cantid = forms.IntegerField()