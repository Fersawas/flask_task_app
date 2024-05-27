import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

mydb = mysql.connector.connect(
    host="localhost", user=os.getenv("USER"), password=os.getenv("PASSWORD")
)

mycursor = mydb.cursor()

# Основная база данных проекта
mycursor.execute("CREATE DATABASE db")

# Тестовая база данных проекта
mycursor.execute("CREATE DATABASE fake_db")
