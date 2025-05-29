from celery import shared_task
from .models import Audiences, IT1_db, IT2_db, IT3_db, IT4_db
from django.db import connection
from datetime import datetime, date, timedelta


@shared_task
def delete_old_data():
    today = date.today()
    max_day = date.today() + timedelta(days=13)
    connection.connect()
    print(f"Server datetime: {datetime.now()}")
    
    # Удаление записей, не входящих во временной промежуток двух недель
    IT1_db.objects.filter(Date__lt=today).delete()
    IT2_db.objects.filter(Date__lt=today).delete()
    IT3_db.objects.filter(Date__lt=today).delete()
    IT4_db.objects.filter(Date__lt=today).delete()
    IT1_db.objects.filter(Date__gt=max_day).delete()
    IT2_db.objects.filter(Date__gt=max_day).delete()
    IT3_db.objects.filter(Date__gt=max_day).delete()
    IT4_db.objects.filter(Date__gt=max_day).delete()
    
    Audiences.objects.filter(
        IT1__isnull=True,
        IT2__isnull=True,
        IT3__isnull=True,
        IT4__isnull=True
    ).delete()
    
    # Создание новых пустых записей
    for delta in range(14):
        db_date = today + timedelta(days=delta)
        var = 0
        
        if not IT1_db.objects.filter(Date=db_date):
            IT1_result = IT1_db.objects.create(
                Date = db_date
            )
            var += 1
            
        if not IT2_db.objects.filter(Date=db_date):
            IT2_result = IT2_db.objects.create(
                Date = db_date
            )
            var += 1
    
        if not IT3_db.objects.filter(Date=db_date):            
            IT3_result = IT3_db.objects.create(
                Date = db_date
            )
            var += 1
    
        if not IT4_db.objects.filter(Date=db_date):            
            IT4_result = IT4_db.objects.create(
                Date = db_date
            )
            var += 1
        
        if var == 4:
            Audiences.objects.create(
                IT1 = IT1_result,
                IT2 = IT2_result,
                IT3 = IT3_result,
                IT4 = IT4_result
            )