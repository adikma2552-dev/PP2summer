import csv
import psycopg2
from connect import get_connection


def create_table():
    """Create phonebook table if it does not exist."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("PhoneBook table is ready.")


def insert_from_console():
    """Insert one contact from console input."""
    first_name = input("Enter first name: ")
    phone = input("Enter phone number: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
            (first_name, phone)
        )
        conn.commit()
        print("Contact inserted successfully.")
    except psycopg2.Error as error:
        conn.rollback()
        print("Error while inserting contact:", error)
    finally:
        cur.close()
        conn.close()


def insert_from_csv(filename="contacts.csv"):
    """Insert contacts from CSV file."""
    conn = get_connection()
    cur = conn.cursor()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cur.execute(
                    """
                    INSERT INTO phonebook (first_name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING
                    """,
                    (row["first_name"], row["phone"])
                )

        conn.commit()
        print("CSV contacts inserted successfully.")
    except Exception as error:
        conn.rollback()
        print("Error while importing CSV:", error)
    finally:
        cur.close()
        conn.close()


def update_contact():
    """Update contact name or phone number."""
    old_phone = input("Enter current phone number of contact: ")
    print("What do you want to update?")
    print("1. First name")
    print("2. Phone number")
    choice = input("Choose option: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        if choice == "1":
            new_name = input("Enter new first name: ")
            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE phone = %s",
                (new_name, old_phone)
            )
        elif choice == "2":
            new_phone = input("Enter new phone number: ")
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE phone = %s",
                (new_phone, old_phone)
            )
        else:
            print("Wrong option.")
            return

        conn.commit()
        print("Contact updated successfully.")
    except psycopg2.Error as error:
        conn.rollback()
        print("Error while updating contact:", error)
    finally:
        cur.close()
        conn.close()


def query_contacts():
    """Query contacts with different filters."""
    print("Search by:")
    print("1. All contacts")
    print("2. Name")
    print("3. Phone prefix")
    choice = input("Choose option: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT id, first_name, phone FROM phonebook ORDER BY id")
    elif choice == "2":
        name = input("Enter name: ")
        cur.execute(
            "SELECT id, first_name, phone FROM phonebook WHERE first_name ILIKE %s",
            (f"%{name}%",)
        )
    elif choice == "3":
        prefix = input("Enter phone prefix: ")
        cur.execute(
            "SELECT id, first_name, phone FROM phonebook WHERE phone LIKE %s",
            (f"{prefix}%",)
        )
    else:
        print("Wrong option.")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def delete_contact():
    """Delete contact by name or phone."""
    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Choose option: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        if choice == "1":
            name = input("Enter name: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        elif choice == "2":
            phone = input("Enter phone: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Wrong option.")
            return

        conn.commit()
        print("Contact deleted successfully.")
    except psycopg2.Error as error:
        conn.rollback()
        print("Error while deleting contact:", error)
    finally:
        cur.close()
        conn.close()


def show_menu():
    """Main console menu."""
    create_table()

    while True:
        print("\nPHONEBOOK MENU")
        print("1. Insert contact from console")
        print("2. Insert contacts from CSV")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Program finished.")
            break
        else:
            print("Wrong option. Try again.")


if __name__ == "__main__":
    show_menu()
