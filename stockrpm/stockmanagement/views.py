from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from management.models import Stock, Owner

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username = request.POST["username"],
                                                password = request.POST["password1"],
                                                first_name = request.POST["name"])
            except :
                return redirect('same_id')
            stocks = Stock.objects.all()
            for cstock in stocks:
                new_owner = Owner.objects.create(name = user.username + '_' +user.first_name, num=0, stock=cstock, itemName=cstock.name)
            auth.login(request,user)
            return redirect('login')
        return render(request, 'login/signup.html')
    return render(request, 'login/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username= username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('management')
        else:
            return render(request, 'login/login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def stockconfirm(request):
    owner_list = list(Owner)
    
    #for x in owner_list:
    print(owner_list)   

    Own_dic = {'owner_list' : owner_list}

    return render(request, 'stockmanagement/st_login.html', Own_dic)