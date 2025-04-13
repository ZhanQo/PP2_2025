import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="zhankozha"
)
cur = conn.cursor()

username = input("Введите имя пользователя: ")

cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if not user:
  
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
    print("Новый пользователь добавлен.")
else:
    user_id = user[0]

    cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
    level, score = cur.fetchone()
    print(f"Добро пожаловать обратно, {username}! Уровень: {level}, Очки: {score}")

conn.commit()
cur.close()
conn.close()