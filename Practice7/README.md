# Practice 7: Python and PostgreSQL PhoneBook

## Objective

This practice is about connecting Python with PostgreSQL and creating a console PhoneBook application.

The program can:

- create a PhoneBook table
- insert contacts from console
- insert contacts from CSV file
- update contact first name or phone number
- query contacts by different filters
- delete contact by name or phone number

## Files

```text
Practice7/
├── phonebook.py
├── config.py
├── connect.py
├── contacts.csv
└── README.md
```

## Requirements

Install PostgreSQL and psycopg2:

```bash
pip install psycopg2-binary
```

## Database setup

Create database in PostgreSQL:

```sql
CREATE DATABASE phonebook_db;
```

Then open `config.py` and change password:

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "phonebook_db",
    "user": "postgres",
    "password": "your_password",
    "port": 5432
}
```

## How to run

```bash
python phonebook.py
```

## Main concepts

### PostgreSQL

PostgreSQL is a relational database management system. It stores data in tables with rows and columns.

### SQL

SQL is a language used to communicate with a database.

Main CRUD operations:

| CRUD | SQL |
|---|---|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

### psycopg2

`psycopg2` is a Python library that allows Python code to connect to PostgreSQL.

Main steps:

1. connect to database
2. create cursor
3. execute SQL query
4. commit changes
5. close cursor and connection

### CSV

CSV is a file format for storing tabular data. In this project `contacts.csv` is used to import many contacts into the database.

## Functions in phonebook.py

### create_table()

Creates `phonebook` table if it does not exist.

### insert_from_console()

Adds one contact using user input.

### insert_from_csv()

Reads contacts from `contacts.csv` and inserts them into PostgreSQL.

### update_contact()

Updates contact name or phone number.

### query_contacts()

Shows all contacts or searches by name / phone prefix.

### delete_contact()

Deletes contact by name or phone number.

## Defense Questions

### What is PostgreSQL?

PostgreSQL is a relational database management system. It stores data in tables.

### What is psycopg2?

psycopg2 is a Python module used to connect Python with PostgreSQL.

### What is CRUD?

CRUD means Create, Read, Update, Delete. These are basic database operations.

### What SQL commands are used for CRUD?

Create is INSERT, Read is SELECT, Update is UPDATE, Delete is DELETE.

### Why do we use commit?

We use `commit()` to save changes in the database after INSERT, UPDATE or DELETE.

### Why do we use rollback?

We use `rollback()` when an error happens, so wrong or unfinished changes are cancelled.

### What is cursor?

Cursor is an object that sends SQL commands from Python to PostgreSQL.

### What is CSV?

CSV is a table-like text file where data is separated by commas.

### Why do we use DictReader?

`csv.DictReader` reads CSV rows as dictionaries, so we can access values by column names like `row["first_name"]`.

### What is ON CONFLICT DO NOTHING?

It prevents duplicate phone numbers from being inserted if the phone already exists.
