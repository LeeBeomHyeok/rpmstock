from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from management.models import Stock, Owner
from django.http import HttpResponse

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


def showDB(request):
    user_list = []
    users = User.objects.all()
    stock_list = []
    stocks = Stock.objects.all()
    owner_value_list = []
    owners_values = Owner.objects.values('num')


    tr_user = list(users)
    tr_stock = list(stocks)
    tr_owner_values = list(owners_values)

    for use in tr_user:
       user_list.append(use)
    user_dic = {'user_list' : user_list}

    for sto in tr_stock:
        stock_list.append(sto)
    stock_dic = {'stock_list' : stock_list}

    for own in tr_owner_values:
        x = list(own.values())
            
        owner_value_list.append(x.pop())
    ind = 0
    for x in user_list:
 
        owner_value_list.insert(ind, x)
        ind +=  5
    
    print(owner_value_list)    
    return render(request, 'confirmstock/test.html', {'stock_list' :stock_list, 
                            'owner_value_list': owner_value_list})