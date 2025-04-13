import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="zhankozha"
)
cur = conn.cursor()

username = input("Введите имя пользователя: ")

cur.execute("""
    SELECT users.id, user_score.level, user_score.score 
    FROM users 
    JOIN user_score ON users.id = user_score.user_id
    WHERE users.username = %s
""", (username,))

user = cur.fetchone()

if user:
    print(f"Уровень: {user[1]}, Счёт: {user[2]}")
else:
    print("Пользователь не найден.")

cur.close()
conn.close()