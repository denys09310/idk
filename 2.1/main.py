import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute("")
while True:
    print("1-Показати список студіків")
    print("2-Показати список курсів")
    print("3-додати курс")
    print("0-вийти")
    choise = input("виберіть дію")
if choise == "0": 
    break
if choise =="1":
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)