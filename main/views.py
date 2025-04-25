from django.shortcuts import render, redirect
from .models import Accounts, Audiences
from django.contrib.auth.hashers import check_password, make_password


def home(request):
    mod = request.POST.get("mod")
    if mod == "1":
        request.session["account_mod"] = 0
        return redirect("main_page")
    elif mod is None:
        return render(request, "main/home.html")
    return render(request, "main/registration.html")


def register(request):
    error = 0
    account = {
        "name": request.POST.get("name"),
        "surname": request.POST.get("surname"),
        "lastname": request.POST.get("lastname"),
        "department": request.POST.get("department"),
        "password": request.POST.get("password")
    }
    
    for i in Accounts.objects.all():
        if (i.name == account["name"]) and (i.surname == account["surname"]) and (i.lastname == account["lastname"]) and (i.department == account["department"]):
            if check_password(account["password"], make_password(i.password)):
                request.session["account"] = account
                request.session["account_mod"] = 1
                return redirect("main_page")
            else:
                error = 1
                break
    
    return render(request, "main/registration.html", {"account": account, "error": error})


def main(request):
    data = {}
    data["account_mod"] = request.session.get("account_mod")
    error = request.session.pop("error", 0)
    audience_list = Audiences.objects.all()
    aditional_info = {
        "AudienceName": ["IT-1", "IT-2", "IT-3"]
    }
    
    if request.method == "GET":
        quit = request.GET.get("quit")
        if quit:
            request.session.flush()
            return redirect("main_page")
    
    if request.method == "POST":
        data = {
            "account_mod": 1,
            "account": request.session.get("account")
        }
        
        new_password = request.POST.get("new_password")
        again_new_password = request.POST.get("again_new_password")
        
        if len(new_password) + len(again_new_password) == 0:
            request.session["error"] = 2
        elif new_password == again_new_password:
            account = Accounts.objects.get(
                name=data["account"]["name"],
                surname=data["account"]["surname"],
                lastname=data["account"]["lastname"],
                department=data["account"]["department"]
            )
            account.password = new_password
            account.save()
            data["account"]["password"] = new_password
            return render(request, "main/main.html", {
                "data": data,
                "audience_list": audience_list,
                "aditional_info": {
                    "AudienceName": ["IT1", "IT2", "IT3"],
                    "SeatsQuantity": {
                        "IT1": 11,
                        "IT2": 22,
                        "IT3": 33
                    }
                }
            })
        else:
            request.session["error"] = 1
        
        return redirect(request.path + "#change-password")
    
    if data["account_mod"] == 1:
        data["account"] = request.session.get("account")
    
    return render(request, "main/main.html", {
        "data": data,
        "error": error,
        "audience_list": audience_list,
        "aditional_info": {
            "AudienceName": ["IT1", "IT2", "IT3"],
            "SeatsQuantity": {
                "IT1": 11,
                "IT2": 22,
                "IT3": 33
            }
        }
    })