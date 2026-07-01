import psycopg2
from connect import get_connection


def execute_sql_file(filename):
    """Run SQL commands from .sql file."""
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()

    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def setup_database():
    """Create table, functions and procedures."""
    execute_sql_file("functions.sql")
    execute_sql_file("procedures.sql")
    print("Database setup completed successfully.")


def show_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()

    print("\n--- All contacts ---")
    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def search_by_pattern():
    pattern = input("Enter name or phone pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()

    print("\n--- Search result ---")
    if not rows:
        print("No matching contacts.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def upsert_one_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

    print("Contact inserted or updated successfully.")

    cur.close()
    conn.close()


def insert_many_contacts():
    names = []
    phones = []

    count = int(input("How many contacts do you want to add? "))

    for i in range(count):
        print(f"\nContact {i + 1}")
        names.append(input("Name: "))
        phones.append(input("Phone: "))

    conn = get_connection()
    cur = conn.cursor()

    cursor_name = "incorrect_contacts_cursor"
    cur.execute("CALL insert_many_contacts(%s, %s, %s)", (names, phones, cursor_name))
    cur.execute(f"FETCH ALL FROM {cursor_name}")
    incorrect_rows = cur.fetchall()

    conn.commit()

    print("\nCorrect contacts were inserted or updated.")

    print("\n--- Incorrect data ---")
    if not incorrect_rows:
        print("No incorrect data.")
    else:
        for row in incorrect_rows:
            print(row)

    cur.close()
    conn.close()


def show_contacts_page():
    limit = int(input("Enter LIMIT: "))
    offset = int(input("Enter OFFSET: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    print("\n--- Page result ---")
    if not rows:
        print("No contacts on this page.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def delete_by_name_or_phone():
    value = input("Enter name or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

    print("Contact deleted if it existed.")

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n========== PHONEBOOK PRACTICE 8 ==========")
        print("1. Setup database")
        print("2. Show all contacts")
        print("3. Search contacts by pattern")
        print("4. Insert or update one contact")
        print("5. Insert many contacts with validation")
        print("6. Show contacts with pagination")
        print("7. Delete contact by name or phone")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            setup_database()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_by_pattern()
        elif choice == "4":
            upsert_one_contact()
        elif choice == "5":
            insert_many_contacts()
        elif choice == "6":
            show_contacts_page()
        elif choice == "7":
            delete_by_name_or_phone()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
