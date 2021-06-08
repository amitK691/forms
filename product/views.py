from django import forms
from .models import TaxAndProduct
from django.shortcuts import render

# Create your views here.
from . import forms
def regform(request):
    form = forms.Pro()
    if request.method == 'POST':
        form = forms.Pro(request.POST)
        name = request.POST.get('Name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        tax_per = request.POST.get('tax_per')
        tax_type = request.POST.get('tax_type')
        tax_amount = request.POST.get('tax_amount')
        print("-----------------------------",name,desc,price,tax_per,tax_type,tax_amount)
        tax_save = TaxAndProduct(Name=name,Desc=desc,Price=price,TaxPer=tax_per,TaxType=tax_type,TaxAmount=tax_amount)
        tax_save.save()
        print("data saved")
        html = 'Form submitted succesfully'
    else:
        html = 'welcome for first time'
    return render(request,'signup.html',{'html':html,'form':form})


