from celery import shared_task
from .models import Audiences, IT5_db, IT11_db, IT15_db, IT17_db
from django.db import connection
from datetime import datetime, date, timedelta
from . import google_sheets


@shared_task
def delete_old_data():
    today = date.today()
    max_day = today + timedelta(days=13)
    connection.connect()
    print(f"Server datetime: {datetime.now()}")
    
    # Удаление записей, не входящих во временной промежуток двух недель
    IT5_db.objects.filter(Date__lt=today).delete()
    IT11_db.objects.filter(Date__lt=today).delete()
    IT15_db.objects.filter(Date__lt=today).delete()
    IT17_db.objects.filter(Date__lt=today).delete()
    IT5_db.objects.filter(Date__gt=max_day).delete()
    IT11_db.objects.filter(Date__gt=max_day).delete()
    IT15_db.objects.filter(Date__gt=max_day).delete()
    IT17_db.objects.filter(Date__gt=max_day).delete()
    
    Audiences.objects.filter(
        IT5__isnull=True,
        IT11__isnull=True,
        IT15__isnull=True,
        IT17__isnull=True
    ).delete()
    
    # Создание новых пустых записей
    for delta in range(14):
        db_date = today + timedelta(days=delta)
        
        if not IT5_db.objects.filter(Date=db_date):
            IT5_result = IT5_db.objects.create(Date=db_date)
        else:
            IT5_result = IT5_db.objects.filter(Date=db_date).first()
        
        if not IT11_db.objects.filter(Date=db_date):
            IT11_result = IT11_db.objects.create(Date=db_date)
        else:
            IT11_result = IT11_db.objects.filter(Date=db_date).first()
        
        if not IT15_db.objects.filter(Date=db_date):
            IT15_result = IT15_db.objects.create(Date=db_date)
        else:
            IT15_result = IT15_db.objects.filter(Date=db_date).first()
        
        if not IT17_db.objects.filter(Date=db_date):            
            IT17_result = IT17_db.objects.create(Date=db_date)
        else:
            IT17_result = IT17_db.objects.filter(Date=db_date).first()
        
        con = Audiences.objects.filter(IT5__Date=db_date)
        
        if not con:
            Audiences.objects.create(
                IT5 = IT5_result,
                IT11 = IT11_result,
                IT15 = IT15_result,
                IT17 = IT17_result
            )