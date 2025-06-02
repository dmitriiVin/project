from django import template
from django.apps import apps
from ..models import Accounts, IT5_db, IT11_db, IT15_db, IT17_db

register = template.Library()


@register.filter()
def pretty_view(IT):
    prettyIT = f"IT-{IT[2:]}"
    return prettyIT


@register.filter()
def get_attr(first, second):
    if hasattr(first, second):
        return getattr(first, second)
    return None


@register.filter()
def get_item_from_dict(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    return None


@register.filter()
def free_or_booked(timetable_item):
    if timetable_item:
        return "booked"
    return "free"


@register.filter()
def increment(num):
    return num + 1


@register.filter()
def decrement(num):
    return num - 1


@register.filter()
def get_date_from_current_date(audience_list, CurrentDateIndex):
    return audience_list[CurrentDateIndex].IT5.Date


@register.filter()
def get_element_from_list(arr, index):
    return arr[index]


@register.filter()
def date_converter(date):
    return str(date).split()[3]


# Задача: имея номер аудитории, дату и имя столбца, найти ФИО преподавателя, ведущего данную пару
@register.filter()
def get_teacher_FIO(verbose_name, date_auditory):
    # Инициализируем переменные
    date, auditory = date_auditory.split("|")
    date = int(date)
    auditory += "_db"
    
    # Найдем среди всех записей бд нужную нам запись
    Django_db_model = apps.get_model("main", auditory)
    all_objects = getattr(Django_db_model, "objects").all()
    audience_on_current_date = all_objects[date]
    
    # Ищем логин владельца записи
    OWNER_element = f"OWNER_{verbose_name}"
    owner_login = getattr(audience_on_current_date, OWNER_element)
    
    # Ищем ФИО при помощи логина и оформляем его
    account = Accounts.objects.filter(login=owner_login).first()
    name = account.name[0] + "."
    surname = account.surname
    lastname = account.lastname[0] + "."
    
    return f"{surname} {name} {lastname}"


@register.filter()
def get_teacher_login(verbose_name, date_auditory):
    # Инициализируем переменные
    date, auditory = date_auditory.split("|")
    date = int(date)
    auditory += "_db"
    
    # Найдем среди всех записей бд нужную нам запись
    Django_db_model = apps.get_model("main", auditory)
    all_objects = getattr(Django_db_model, "objects").all()
    audience_on_current_date = all_objects[date]
    
    # Ищем логин владельца записи
    OWNER_element = f"OWNER_{verbose_name}"
    owner_login = getattr(audience_on_current_date, OWNER_element)

    return owner_login


@register.filter()
def concatenate(date, auditory):
    return f"{date}|{auditory}"