from django.shortcuts import render, redirect
from .models import Accounts, Audiences


# Количество посадочных мест в аудиториях
seats_quantity = {
    "IT5": 80,
    "IT11": 25,
    "IT15": 28,
    "IT17": 22
}


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
    requested_login = request.POST.get("login")
    requested_password = request.POST.get("password")
    account = Accounts.objects.filter(login=requested_login).first()
    
    if account:
        account_dict = {
            "name": account.name,
            "surname": account.surname,
            "lastname": account.lastname,
            "department": account.department,
            "login": account.login,
            "password": account.password
        }
    
        if requested_login and requested_password:
            if account.password == requested_password:
                request.session["account"] = account_dict
                request.session["account_mod"] = 1
                return redirect("main_page")
            else:
                error = 1
    
    audience_list = Audiences.objects.all()
    current_date = 0
    
    return render(request, "main/registration.html", {"error": error})



def main(request):
    data = {}
    data["account_mod"] = request.session.get("account_mod")
    error = request.session.pop("error", 0)
    audience_list = Audiences.objects.all()
    current_date = 0
    aditional_info = {
        "AudienceName": ["IT-5", "IT-11", "IT-15", "IT-17"]
    }
    
    # Сработает, если quit был отправлен (запрос на выход из аккаунта)
    quit = request.GET.get("quit")
    if quit:
        request.session.flush()
        return redirect("main_page")
    
    # Сработает, если был запрос на смену даты на 1 день вперед или назад
    new_current_date = request.GET.get("current_date_index_from_form")
    
    if new_current_date and new_current_date != "None":
        current_date = int(new_current_date)
    
    if data["account_mod"] == 1:
        data["account"] = request.session.get("account")
    
    DataToFrontend = {
        "data": data,
        "audience_list": audience_list,
        "aditional_info": {
            "AudienceName": ["IT5", "IT11", "IT15", "IT17"],
            "SeatsQuantity": seats_quantity,
            "CurrentDateIndex": current_date,
            "AllLessonTimings": [
                ["GroupIn900_1030", "9:00-10:30"],
                ["GroupIn1045_1215", "10:45-12:15"],
                ["GroupIn1300_1430", "13:00-14:30"],
                ["GroupIn1445_1615", "14:45-16:15"],
                ["GroupIn1630_1800", "16:30-18:00"],
                ["GroupIn1815_1945", "18:15-19:45"]
            ]
        }
    }
    
    if request.method == "POST":
        IT_date_time = request.POST.get("IT_date_time")
        current_date_for_edit = request.POST.get("current_date_for_edit")
        group_for_add = request.POST.get("group_for_add")
        owner_login = request.POST.get("owner_login")
        
        if group_for_add:
            if len(group_for_add) > 16:
                return redirect(f"{request.path}?current_date_index_from_form={current_date_for_edit}")
        
        if IT_date_time:
            IT, date, time = IT_date_time.split("|")
            time_slot_name = "GroupIn" + time.replace(":", "").replace("-", "_") # Имя столбца на определенное время
            audience = Audiences.objects.filter(
                **{f"{IT}__Date": date}
            ).first()
            
            it = getattr(audience, IT)
            setattr(it, time_slot_name, group_for_add)
            setattr(it, f"OWNER_{time_slot_name}", owner_login)
            it.save()
            
            return redirect(f"{request.path}?current_date_index_from_form={current_date_for_edit}")
        
        else:
            data = {
                "account_mod": 1,
                "account": request.session.get("account")
            }
            new_password = request.POST.get("new_password")
            again_new_password = request.POST.get("again_new_password")
            
            if not new_password or not again_new_password:
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
                print(DataToFrontend)
                return render(request, "main/main.html", DataToFrontend)
            
            else:
                request.session["error"] = 1
            
            return redirect(f"{request.path}?current_date_index_from_form={current_date_for_edit}#change-password")
    
    # Добавляем error в DataToFrontend
    DataToFrontend["error"] = error
    
    return render(request, "main/main.html", DataToFrontend)