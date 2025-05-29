from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError



class Accounts(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    lastname = models.CharField("Отчество", max_length=50)
    department = models.CharField("Кафедра", max_length=2)
    password = models.CharField("Пароль", max_length=128)
    
    def __str__(self):
        return f"{self.name} {self.surname} {self.lastname}"
    
    class Meta():
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"



class IT_db_base(models.Model):
    Date = models.DateField("Дата")
    GroupIn900_1030 = models.CharField("Группа на 9.00-10.30", max_length=16, blank=True, default="")
    GroupIn1045_1215 = models.CharField("Группа на 10.45-12.15", max_length=16, blank=True, default="")
    GroupIn1300_1430 = models.CharField("Группа на 13.00-14.30", max_length=16, blank=True, default="")
    GroupIn1445_1615 = models.CharField("Группа на 14.45-16.15", max_length=16, blank=True, default="")
    GroupIn1630_1800 = models.CharField("Группа на 16.30-18.00", max_length=16, blank=True, default="")
    GroupIn1800_1930 = models.CharField("Группа на 18.00-19.30", max_length=16, blank=True, default="")
    
    def clean(self):
        now = datetime.today().date()
        max_time = now + timedelta(days=14)
        if not(now <= self.Date <= max_time):
            raise ValidationError("Вы можете указать дату только в двухнедельном промежутке, начиная от сегодняшнего дня")
        super().clean()
    
    class Meta():
        abstract = True



class IT1_db(IT_db_base):
    def __str__(self):
        return f"IT-1 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-1"
        verbose_name_plural = "Группы в IT-1"



class IT2_db(IT_db_base):
    def __str__(self):
        return f"IT-2 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-2"
        verbose_name_plural = "Группы в IT-2"



class IT3_db(IT_db_base):
    def __str__(self):
        return f"IT-3 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-3"
        verbose_name_plural = "Группы в IT-3"



class IT4_db(IT_db_base):
    def __str__(self):
        return f"IT-3 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-4"
        verbose_name_plural = "Группы в IT-4"



class Audiences(models.Model):
    IT1 = models.ForeignKey(IT1_db, on_delete=models.CASCADE, null=True, blank=True)
    IT2 = models.ForeignKey(IT2_db, on_delete=models.CASCADE, null=True, blank=True)
    IT3 = models.ForeignKey(IT3_db, on_delete=models.CASCADE, null=True, blank=True)
    IT4 = models.ForeignKey(IT4_db, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Расписание на дату: {self.IT1.Date}"
    
    def clean(self):
        dates = []
        for i in [self.IT1, self.IT2, self.IT3, self.IT4]:
            if i:
                dates.append(i.Date)
        
        if not(dates):
            raise ValidationError(f"Вы не можете добавлять пустой класс")
        
        first = ""
        for i in dates:
            if i:
                if not first:
                    first = i
                else:
                    if first != i:
                        raise ValidationError(f"Вы можете добавлять в этот класс только расписание на определенную дату: {first}")
    
    class Meta():
        verbose_name = "Занятость IT класса по датам"
        verbose_name_plural = "Занятость IT классов по датам"