from django import forms
from django.forms.fields import IntegerField
from django.forms.widgets import Widget
# form

tax_type = [
        ('0','select..'),
        ('1','excluded'),
        ('2','included'),
        ]


class Pro(forms.Form):
    Name = forms.CharField()
    desc = forms.CharField(widget = forms.Textarea)
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input'}))
    tax_per = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input'}))
    tax_type = forms.ChoiceField(choices=tax_type,widget=forms.Select(attrs={'class':'input'}))
    tax_amount = IntegerField()
    