import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Lab10",
    user="postgres",
    password="040806"
)
cur = conn.cursor()

username = input("Введите имя: ")
phone = input("Введите номер: ")

cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))

conn.commit()
print("Данные успешно добавлены!")

cur.close()
conn.close()