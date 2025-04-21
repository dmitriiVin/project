from django.db import models

class Accounts(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    lastname = models.CharField("Отчество", max_length=50)
    group = models.CharField("Группа", max_length=50)
    password = models.CharField("Пароль", max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"