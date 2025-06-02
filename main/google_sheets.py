from oauth2client.service_account import ServiceAccountCredentials
import gspread
from django.conf import settings
from .models import IT5_db, IT11_db, IT15_db, IT17_db
import time
import os


# Параметры для авторизации
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
CREDENTIALS = os.path.join(settings.BASE_DIR, "credentials.json")
Table_ID = "1EljnMsSjaXU50mIq9PjNXn966bzVrQAi5clWEsIWKH4"

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS, SCOPE)
spreadsheets = gspread.authorize(credentials)
gc = gspread.authorize(credentials)


def GoogleSheets_update(dbModel, IT):
    try:
        # Фасуем данные из бд в переменные для удобства
        Date = str(dbModel.Date)
        GroupIn900_1030 = str(dbModel.GroupIn900_1030)
        GroupIn1045_1215 = str(dbModel.GroupIn1045_1215)
        GroupIn1300_1430 = str(dbModel.GroupIn1300_1430)
        GroupIn1445_1615 = str(dbModel.GroupIn1445_1615)
        GroupIn1630_1800 = str(dbModel.GroupIn1630_1800)
        GroupIn1815_1945 = str(dbModel.GroupIn1815_1945)
        
        # Если страница вдруг не будет существовать, то мы ее создадим
        spreadsheet = gc.open_by_key(Table_ID)
        worksheet = spreadsheet.worksheet(Date)
        try:
            worksheet = spreadsheet.worksheet(Date)
        except gspread.WorksheetNotFound:
            # Если листа нет — создаём его
            worksheet = spreadsheet.add_worksheet(title=Date, rows=1000, cols=26)
            print(f"GoogleSheets | Лист {Date} создан")
            # Добавляем разметку
            worksheet.update("B1:E1", [["IT5", "IT11", "IT15", "IT17"]])
            worksheet.update("A2:A7", [
                ["9.00-10.30"], ["10.45-12.15"], ["13.00-14.30"],
                ["14.45-16.15"], ["16.30-18.00"], ["18.15-19.45"]
            ])
            time.sleep(0.2)        
        
        # Если вдруг страница пустая, добавляем на нее разметку
        if worksheet.get_all_values() == [[]]:
            worksheet.update("B1:E1", [["IT5", "IT11", "IT15", "IT17"]])
            worksheet.update("A2:A7", [
                ["9.00-10.30"], ["10.45-12.15"], ["13.00-14.30"],
                ["14.45-16.15"], ["16.30-18.00"], ["18.15-19.45"]
            ])
        
        # Обновляем данные
        if IT == "IT5":
            interval = "B2:B7"
        elif IT == "IT11":
            interval = "C2:C7"
        elif IT == "IT15":
            interval = "D2:D7"
        elif IT == "IT17":
            interval = "E2:E7"
        
        worksheet.update(interval, [
            [GroupIn900_1030], [GroupIn1045_1215], [GroupIn1300_1430],
            [GroupIn1445_1615], [GroupIn1630_1800], [GroupIn1815_1945]
        ])
        
        print("GoogleSheets | Обновление данных прошло успешно")
    
    except Exception as e:
        print(f"GoogleSheets | Произошла ошибка при попытке обновления данных: {e}")