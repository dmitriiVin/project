from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError



class Accounts(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    lastname = models.CharField("Отчество", max_length=50)
    department = models.CharField("Кафедра", max_length=6)
    login = models.CharField("Логин", max_length=50, unique=True)
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
    GroupIn1815_1945 = models.CharField("Группа на 18.15-19.45", max_length=16, blank=True, default="")
    OWNER_GroupIn900_1030 = models.CharField("Владелец группы на 9.00-10.30", max_length=50, blank=True, default="")
    OWNER_GroupIn1045_1215 = models.CharField("Владелец группы на 10.45-12.15", max_length=50, blank=True, default="")
    OWNER_GroupIn1300_1430 = models.CharField("Владелец группы на 13.00-14.30", max_length=50, blank=True, default="")
    OWNER_GroupIn1445_1615 = models.CharField("Владелец группы на 14.45-16.15", max_length=50, blank=True, default="")
    OWNER_GroupIn1630_1800 = models.CharField("Владелец группы на 16.30-18.00", max_length=50, blank=True, default="")
    OWNER_GroupIn1815_1945 = models.CharField("Владелец группы на 18.15-19.45", max_length=50, blank=True, default="")
    
    
    
    def clean(self):
        # Проверка правильности указания даты (только в двухнедельном промежутке от сегодняшнего дня)
        now = datetime.today().date()
        max_time = now + timedelta(days=14)
        if not(now <= self.Date <= max_time):
            raise ValidationError("Вы можете указать дату только в двухнедельном промежутке, начиная от сегодняшнего дня")
        
        # Корректировка столбцов "Группа" - "Владелец записи"
        own_paras = [
            [self.GroupIn900_1030, self.OWNER_GroupIn900_1030],
            [self.GroupIn1045_1215, self.OWNER_GroupIn1045_1215],
            [self.GroupIn1300_1430, self.OWNER_GroupIn1300_1430],
            [self.GroupIn1445_1615, self.OWNER_GroupIn1445_1615],
            [self.GroupIn1630_1800, self.OWNER_GroupIn1630_1800],
            [self.GroupIn1815_1945, self.OWNER_GroupIn1815_1945]
        ]
        
        times = [
            "9.00-10.30", "10.45-12.15", "13.00-14.30",
            "14.45-16.15", "16.30-18.00", "18.15-19.45"
        ]
        
        all_logins = [i.login for i in Accounts.objects.all()] # Тут хранятся все существующие логины от аккаунтов преподавателей
        iteration_count = 0
        
        for i in own_paras:
            if i[1] and (i[1] not in all_logins):
                raise ValidationError(f'Преподавателя с логином "{i[1]}" не существует')
            elif i[0] and (not i[1]):
                raise ValidationError(f"Для группы в {times[iteration_count]} необходимо указать владельца")
            elif (not i[0]) and i[1]:
                raise ValidationError(f"Необходимо указать группу на {times[iteration_count]}")
            iteration_count += 1
        
        # Стандартные проверки Django
        super().clean()
    
    class Meta():
        abstract = True



class IT5_db(IT_db_base):
    def __str__(self):
        return f"IT-5 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-5"
        verbose_name_plural = "Группы в IT-5"
        ordering = ["Date"]



class IT11_db(IT_db_base):
    def __str__(self):
        return f"IT-11 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-11"
        verbose_name_plural = "Группы в IT-11"
        ordering = ["Date"]



class IT15_db(IT_db_base):
    def __str__(self):
        return f"IT-15 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-15"
        verbose_name_plural = "Группы в IT-15"
        ordering = ["Date"]



class IT17_db(IT_db_base):
    def __str__(self):
        return f"IT-17 ({str(self.Date)})"
    
    class Meta():
        verbose_name = "Группа в IT-17"
        verbose_name_plural = "Группы в IT-17"
        ordering = ["Date"]



class Audiences(models.Model):
    IT5 = models.ForeignKey(IT5_db, on_delete=models.CASCADE, null=True, blank=True)
    IT11 = models.ForeignKey(IT11_db, on_delete=models.CASCADE, null=True, blank=True)
    IT15 = models.ForeignKey(IT15_db, on_delete=models.CASCADE, null=True, blank=True)
    IT17 = models.ForeignKey(IT17_db, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Расписание на дату: {self.IT5.Date}"
    
    def clean(self):
        dates = []
        for i in [self.IT5, self.IT11, self.IT15, self.IT17]:
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
        ordering = ['IT5__Date']