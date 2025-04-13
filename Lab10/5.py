import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="zhankozha"
)

cur = conn.cursor()

cur.execute("""
    SELECT u.username, us.level, us.score
    FROM users u
    JOIN user_score us ON u.id = us.user_id;
""")

rows = cur.fetchall()
print("Результаты пользователей:")
for row in rows:
    print(f"Имя: {row[0]}, Уровень: {row[1]}, Счёт: {row[2]}")

cur.close()
conn.close()