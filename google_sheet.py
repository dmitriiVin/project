import sqlite3
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

DB_PATH = './db.sqlite3'
CREDENTIALS = './credentials.json'
SPREADSHEET_ID = '1F3487SZCoB0tWzTIeiB2zSLtmygc1uJabG_Ylk9I-s4L'


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file(CREDENTIALS, scopes=SCOPES)
gc = gspread.authorize(creds)
sh = gc.open_by_key(SPREADSHEET_ID)
conn = sqlite3.connect(DB_PATH)

tables = ['main_it1_db', 'main_it2_db', 'main_it3_db', 'main_it4_db']

for tbl in tables:
    df = pd.read_sql_query(f"SELECT * FROM {tbl}", conn)
    try:
        wks = sh.worksheet(tbl)
        wks.clear()
    except gspread.WorksheetNotFound:
        wks = sh.add_worksheet(title=tbl, rows=str(len(df) + 5), cols=str(len(df.columns) + 5))
    wks.update([df.columns.values.tolist()] + df.values.tolist())
    print(f"Таблица {tbl} загружена, строк: {len(df)}")

conn.close()
