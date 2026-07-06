import csv
import json
from connect import get_connection


def execute_sql_file(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()
        cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    print(f"{filename} executed successfully.")


def get_group_id(cur, group_name):
    cur.execute(
        "INSERT INTO groups(name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
        (group_name,)
    )
    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    return cur.fetchone()[0]


def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday YYYY-MM-DD: ")
    group_name = input("Group: ")
    phone = input("Phone: ")
    phone_type = input("Phone type home/work/mobile: ")

    conn = get_connection()
    cur = conn.cursor()

    group_id = get_group_id(cur, group_name)

    cur.execute(
        """
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO UPDATE
        SET email = EXCLUDED.email,
            birthday = EXCLUDED.birthday,
            group_id = EXCLUDED.group_id
        RETURNING id
        """,
        (name, email, birthday, group_id)
    )

    contact_id = cur.fetchone()[0]

    cur.execute(
        "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
        (contact_id, phone, phone_type)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added successfully.")


def show_contacts():
    sort_by = input("Sort by name/birthday/date: ")

    allowed_sort = {
        "name": "c.name",
        "birthday": "c.birthday",
        "date": "c.created_at"
    }

    order_column = allowed_sort.get(sort_by, "c.name")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        f"""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type, c.created_at
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY {order_column}
        """
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def filter_by_group():
    group_name = input("Enter group name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.name ILIKE %s
        """,
        (group_name,)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_by_email():
    email = input("Search email: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE c.email ILIKE %s
        """,
        (f"%{email}%",)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_all_fields():
    query = input("Search name/email/phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (query,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def paginated_contacts():
    limit = 3
    offset = 0

    while True:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            ORDER BY c.name
            LIMIT %s OFFSET %s
            """,
            (limit, offset)
        )

        rows = cur.fetchall()

        print("\n--- PAGE ---")
        for row in rows:
            print(row)

        cur.close()
        conn.close()

        command = input("next / prev / quit: ")

        if command == "next":
            offset += limit
        elif command == "prev":
            offset = max(0, offset - limit)
        elif command == "quit":
            break
        else:
            print("Wrong command.")


def import_csv():
    filename = input("CSV filename: ")

    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            group_id = get_group_id(cur, row["group"])

            cur.execute(
                """
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET email = EXCLUDED.email,
                    birthday = EXCLUDED.birthday,
                    group_id = EXCLUDED.group_id
                RETURNING id
                """,
                (row["name"], row["email"], row["birthday"], group_id)
            )

            contact_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
                (contact_id, row["phone"], row["type"])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported successfully.")


def export_json():
    filename = input("JSON filename to export: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.name
        """
    )

    contacts = cur.fetchall()
    data = []

    for contact in contacts:
        contact_id, name, email, birthday, group_name = contact

        cur.execute(
            "SELECT phone, type FROM phones WHERE contact_id = %s",
            (contact_id,)
        )

        phones = cur.fetchall()

        data.append({
            "name": name,
            "email": email,
            "birthday": str(birthday) if birthday else None,
            "group": group_name,
            "phones": [
                {"phone": phone, "type": phone_type}
                for phone, phone_type in phones
            ]
        })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    cur.close()
    conn.close()
    print("Exported to JSON successfully.")


def import_json():
    filename = input("JSON filename to import: ")

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    conn = get_connection()
    cur = conn.cursor()

    for item in data:
        name = item["name"]

        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
        existing = cur.fetchone()

        if existing:
            choice = input(f"{name} exists. skip/overwrite: ")

            if choice == "skip":
                continue

            if choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name = %s", (name,))

        group_id = get_group_id(cur, item["group"])

        cur.execute(
            """
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            (item["name"], item["email"], item["birthday"], group_id)
        )

        contact_id = cur.fetchone()[0]

        for phone_data in item["phones"]:
            cur.execute(
                "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
                (contact_id, phone_data["phone"], phone_data["type"])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("JSON imported successfully.")


def add_phone_procedure():
    name = input("Contact name: ")
    phone = input("New phone: ")
    phone_type = input("Type home/work/mobile: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()
    print("Phone added by procedure.")


def move_to_group_procedure():
    name = input("Contact name: ")
    group_name = input("New group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s, %s)", (name, group_name))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact moved to group.")


def menu():
    while True:
        print("""
========== PHONEBOOK TSIS1 ==========
1. Create tables
2. Create procedures
3. Add contact
4. Show contacts
5. Filter by group
6. Search by email
7. Search name/email/phone
8. Paginated contacts
9. Import CSV
10. Export JSON
11. Import JSON
12. Add phone procedure
13. Move to group procedure
0. Exit
=====================================
""")

        choice = input("Choose: ")

        if choice == "1":
            execute_sql_file("schema.sql")
        elif choice == "2":
            execute_sql_file("procedures.sql")
        elif choice == "3":
            add_contact()
        elif choice == "4":
            show_contacts()
        elif choice == "5":
            filter_by_group()
        elif choice == "6":
            search_by_email()
        elif choice == "7":
            search_all_fields()
        elif choice == "8":
            paginated_contacts()
        elif choice == "9":
            import_csv()
        elif choice == "10":
            export_json()
        elif choice == "11":
            import_json()
        elif choice == "12":
            add_phone_procedure()
        elif choice == "13":
            move_to_group_procedure()
        elif choice == "0":
            break
        else:
            print("Wrong choice.")


if __name__ == "__main__":
    menu()
