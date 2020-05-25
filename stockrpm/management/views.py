from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Stock, Owner
from django.contrib import auth


# Create your views here.
def index(request):
    user = auth.get_user(request)
    if request.method == "POST":
        stocks = Stock.objects.all()
        for cstock in stocks:
            try:
                new_num = int(request.POST[cstock.name])
            except:
                new_num = 0
            cstock.num -= new_num
            try:
                cname = cstock.owner_set.get(name = user.username + '_' +user.first_name)
            except:
                new_owner = Owner.objects.create(name = user.username + '_' +user.first_name, num=new_num, stock=cstock, itemName=cstock.name)
            else:
                cname.num += new_num
                cname.save()
            cstock.save()
        return redirect('management')
    stocks = Stock.objects.all()

    my_stocks = Owner.objects.filter(name = user.username + '_' +user.first_name)

    context = {'stocks':stocks, 'my_stocks' : my_stocks}
    return render(request, 'management/index.html', context)
