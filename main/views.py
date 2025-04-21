from django.shortcuts import render
from .models import Accounts
from django.contrib.auth.hashers import check_password


def home(request):
    mod = request.POST.get("mod")
    if mod in ["0", None]:
        error = 0
        account = {
            "name": request.POST.get("name"),
            "surname": request.POST.get("surname"),
            "lastname": request.POST.get("lastname"),
            "group": request.POST.get("group"),
            "password": request.POST.get("password")
        }
    
        for i in Accounts.objects.all():
            if (i.name == account["name"]) and (i.surname == account["surname"]) and (i.lastname == account["lastname"]) and (i.group == account["group"]):
                if i.password == account["password"]:
                    return render(request, "main/main.html", {"account": account})
                else:
                    error = 1
        
        if mod is None:
            error = -1
        
        return render(request, "main/home.html", {"account": account, "error": error})
    
    return render(request, "main/main.html", {"account": None})


def main(request):
    return render(request, "main/main.html")