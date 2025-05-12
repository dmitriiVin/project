from django import template

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
    return audience_list[CurrentDateIndex].IT1.Date

@register.filter()
def get_element_from_list(arr, index):
    return arr[index]

@register.filter()
def date_converter(date):
    return str(date).split()[3]