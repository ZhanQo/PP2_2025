import psycopg2
import csv

# Подключение к БД
conn = psycopg2.connect(
    host="localhost",
    database="Lab10",
    user="postgres",
    password="040806"
)
cur = conn.cursor()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Inserted successfully.")

def update_user():
    phone = input("Enter phone number to update: ")
    new_name = input("Enter new name: ")
    cur.execute("UPDATE phonebook SET username = %s WHERE phone = %s", (new_name, phone))
    conn.commit()
    print("Updated successfully.")

def search_user():
    name = input("Enter name to search: ")
    cur.execute("SELECT * FROM phonebook WHERE username = %s", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_user():
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
    conn.commit()
    print("Deleted successfully.")

def insert_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook () username, phone) VALUES (%s, %s)",
                        (row['name'], row['phone']))
    conn.commit()
    print("CSV data inserted successfully.")

def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert new user (console)")
        print("2. Update user")
        print("3. Search user")
        print("4. Delete user")
        print("5. Upload from CSV")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            update_user()
        elif choice == "3":
            search_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            filename = input("Enter CSV file path: ")
            insert_from_csv(filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()