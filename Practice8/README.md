# Practice 8 - PostgreSQL Functions and Stored Procedures

This practice continues the PhoneBook application from Practice 7.
The main goal is to move SQL logic into PostgreSQL functions and stored procedures.

## Files

- `config.py` - database settings
- `connect.py` - PostgreSQL connection
- `functions.sql` - PostgreSQL functions
- `procedures.sql` - PostgreSQL stored procedures
- `phonebook.py` - Python menu application

## Implemented tasks

1. Function to search contacts by pattern:
   - `get_contacts_by_pattern(pattern)`

2. Procedure to insert or update contact:
   - `upsert_contact(name, phone)`

3. Procedure to insert many contacts with phone validation:
   - `insert_many_contacts(names[], phones[], cursor)`

4. Function for pagination:
   - `get_contacts_page(limit, offset)`

5. Procedure to delete by username or phone:
   - `delete_contact(value)`

## How to run

Install psycopg2:

```bash
pip install psycopg2
```

Run the program:

```bash
python phonebook.py
```

First choose option `1` to setup database, functions and procedures.

## Phone validation

Correct phone format:

- only digits
- length from 10 to 15

Example correct phone:

```text
87071234567
```

Example incorrect phone:

```text
abc123
```
