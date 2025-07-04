# Generated by Django 5.1.7 on 2025-05-31 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('lastname', models.CharField(max_length=50, verbose_name='Отчество')),
                ('department', models.CharField(max_length=6, verbose_name='Кафедра')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='IT11_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(verbose_name='Дата')),
                ('GroupIn900_1030', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 9.00-10.30')),
                ('GroupIn1045_1215', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 10.45-12.15')),
                ('GroupIn1300_1430', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 13.00-14.30')),
                ('GroupIn1445_1615', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 14.45-16.15')),
                ('GroupIn1630_1800', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 16.30-18.00')),
                ('GroupIn1815_1945', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 18.15-19.45')),
                ('OWNER_GroupIn900_1030', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 9.00-10.30')),
                ('OWNER_GroupIn1045_1215', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 10.45-12.15')),
                ('OWNER_GroupIn1300_1430', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 13.00-14.30')),
                ('OWNER_GroupIn1445_1615', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 14.45-16.15')),
                ('OWNER_GroupIn1630_1800', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 16.30-18.00')),
                ('OWNER_GroupIn1815_1945', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 18.15-19.45')),
            ],
            options={
                'verbose_name': 'Группа в IT-11',
                'verbose_name_plural': 'Группы в IT-11',
                'ordering': ['Date'],
            },
        ),
        migrations.CreateModel(
            name='IT15_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(verbose_name='Дата')),
                ('GroupIn900_1030', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 9.00-10.30')),
                ('GroupIn1045_1215', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 10.45-12.15')),
                ('GroupIn1300_1430', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 13.00-14.30')),
                ('GroupIn1445_1615', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 14.45-16.15')),
                ('GroupIn1630_1800', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 16.30-18.00')),
                ('GroupIn1815_1945', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 18.15-19.45')),
                ('OWNER_GroupIn900_1030', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 9.00-10.30')),
                ('OWNER_GroupIn1045_1215', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 10.45-12.15')),
                ('OWNER_GroupIn1300_1430', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 13.00-14.30')),
                ('OWNER_GroupIn1445_1615', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 14.45-16.15')),
                ('OWNER_GroupIn1630_1800', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 16.30-18.00')),
                ('OWNER_GroupIn1815_1945', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 18.15-19.45')),
            ],
            options={
                'verbose_name': 'Группа в IT-15',
                'verbose_name_plural': 'Группы в IT-15',
                'ordering': ['Date'],
            },
        ),
        migrations.CreateModel(
            name='IT17_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(verbose_name='Дата')),
                ('GroupIn900_1030', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 9.00-10.30')),
                ('GroupIn1045_1215', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 10.45-12.15')),
                ('GroupIn1300_1430', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 13.00-14.30')),
                ('GroupIn1445_1615', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 14.45-16.15')),
                ('GroupIn1630_1800', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 16.30-18.00')),
                ('GroupIn1815_1945', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 18.15-19.45')),
                ('OWNER_GroupIn900_1030', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 9.00-10.30')),
                ('OWNER_GroupIn1045_1215', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 10.45-12.15')),
                ('OWNER_GroupIn1300_1430', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 13.00-14.30')),
                ('OWNER_GroupIn1445_1615', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 14.45-16.15')),
                ('OWNER_GroupIn1630_1800', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 16.30-18.00')),
                ('OWNER_GroupIn1815_1945', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 18.15-19.45')),
            ],
            options={
                'verbose_name': 'Группа в IT-17',
                'verbose_name_plural': 'Группы в IT-17',
                'ordering': ['Date'],
            },
        ),
        migrations.CreateModel(
            name='IT5_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(verbose_name='Дата')),
                ('GroupIn900_1030', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 9.00-10.30')),
                ('GroupIn1045_1215', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 10.45-12.15')),
                ('GroupIn1300_1430', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 13.00-14.30')),
                ('GroupIn1445_1615', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 14.45-16.15')),
                ('GroupIn1630_1800', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 16.30-18.00')),
                ('GroupIn1815_1945', models.CharField(blank=True, default='', max_length=16, verbose_name='Группа на 18.15-19.45')),
                ('OWNER_GroupIn900_1030', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 9.00-10.30')),
                ('OWNER_GroupIn1045_1215', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 10.45-12.15')),
                ('OWNER_GroupIn1300_1430', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 13.00-14.30')),
                ('OWNER_GroupIn1445_1615', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 14.45-16.15')),
                ('OWNER_GroupIn1630_1800', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 16.30-18.00')),
                ('OWNER_GroupIn1815_1945', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец группы на 18.15-19.45')),
            ],
            options={
                'verbose_name': 'Группа в IT-5',
                'verbose_name_plural': 'Группы в IT-5',
                'ordering': ['Date'],
            },
        ),
        migrations.CreateModel(
            name='Audiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IT11', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.it11_db')),
                ('IT15', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.it15_db')),
                ('IT17', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.it17_db')),
                ('IT5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.it5_db')),
            ],
            options={
                'verbose_name': 'Занятость IT класса по датам',
                'verbose_name_plural': 'Занятость IT классов по датам',
                'ordering': ['IT5__Date'],
            },
        ),
    ]
