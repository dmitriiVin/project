from django.shortcuts import render, redirect
from .models import Accounts, Audiences
from django.contrib.auth.hashers import check_password, make_password


# Количество посадочных мест в аудиториях
seats_quantity = {
    "IT1": 11,
    "IT2": 22,
    "IT3": 33,
    "IT4": 44
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
    
    audience_list = Audiences.objects.all()
    current_date = 0
    
    return render(request, "main/registration.html", {
        "account": account,
        "error": error,
        "audience_list": audience_list,
        "aditional_info": {
            "CurrentDateIndex": current_date,
            "AudienceName": ["IT1", "IT2", "IT3", "IT4"],
            "SeatsQuantity": seats_quantity,
            "AllLessonTimings": [
                ["GroupIn900_1030", "9:00-10:30"],
                ["GroupIn1045_1215", "10:45-12:15"],
                ["GroupIn1300_1430", "13:00-14:30"],
                ["GroupIn1445_1615", "14:45-16:15"],
                ["GroupIn1630_1800", "16:30-18:00"],
                ["GroupIn1800_1930", "18:00-19:30"]
            ]
        }
    })



def main(request):
    data = {}
    data["account_mod"] = request.session.get("account_mod")
    error = request.session.pop("error", 0)
    audience_list = Audiences.objects.all()
    current_date = 0
    aditional_info = {
        "AudienceName": ["IT-1", "IT-2", "IT-3", "IT4"]
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
    
    DataToFrontend = {
        "data": data,
        "audience_list": audience_list,
        "aditional_info": {
            "AudienceName": ["IT1", "IT2", "IT3", "IT4"],
            "SeatsQuantity": seats_quantity,
            "CurrentDateIndex": current_date,
            "AllLessonTimings": [
                ["GroupIn900_1030", "9:00-10:30"],
                ["GroupIn1045_1215", "10:45-12:15"],
                ["GroupIn1300_1430", "13:00-14:30"],
                ["GroupIn1445_1615", "14:45-16:15"],
                ["GroupIn1630_1800", "16:30-18:00"],
                ["GroupIn1800_1930", "18:00-19:30"]
            ]
        }
    }
    
    if request.method == "POST":
        IT_date_time = request.POST.get("IT_date_time")
        current_date_for_edit = request.POST.get("current_date_for_edit")
        group_for_add = request.POST.get("group_for_add")
        
        if group_for_add:
            if len(group_for_add) > 16:
                return redirect(f"{request.path}?current_date_index_from_form={current_date_for_edit}")
        
        if IT_date_time:
            IT, date, time = IT_date_time.split("|")
            time_slot_name = "GroupIn" + time.replace(":", "").replace("-", "_") # Имя столбца на определенное время
            audience = Audiences.objects.filter(
                **{f"{IT}__Date": date}
            ).first()
            
            for i in Audiences.objects.all():
                print(i.IT4.Date)
            
            it = getattr(audience, IT)
            setattr(it, time_slot_name, group_for_add)
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
                
                return render(request, "main/main.html", DataToFrontend)
            
            else:
                request.session["error"] = 1
            
            return redirect(f"{request.path}?current_date_index_from_form={current_date_for_edit}#change-password")
    
    
    if data["account_mod"] == 1:
        data["account"] = request.session.get("account")
    
    # Добавляем error в DataToFrontend
    DataToFrontend["error"] = error
    
    return render(request, "main/main.html", DataToFrontend)