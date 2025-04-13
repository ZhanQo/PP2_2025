import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="zhankozha"

)
cur = conn.cursor()

username = input("Имя пользователя чтобы удалить: ")

cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
conn.commit()

if cur.rowcount > 0:
    print("Пользователь удалён!")
else:
    print("Такого пользователя нет.")

cur.close()
conn.close()