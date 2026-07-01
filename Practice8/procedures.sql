-- Practice 8: PostgreSQL Stored Procedures for PhoneBook

CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- 2. Procedure: insert new contact, update phone if name already exists
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- 3. Procedure: insert many users and return incorrect data using refcursor
-- Correct phone format here: only digits, length from 10 to 15
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[],
    p_phones VARCHAR[],
    INOUT incorrect_data REFCURSOR
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    bad_name VARCHAR;
    bad_phone VARCHAR;
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS temp_incorrect_contacts(
        name VARCHAR,
        phone VARCHAR,
        reason TEXT
    ) ON COMMIT DROP;

    TRUNCATE temp_incorrect_contacts;

    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] !~ '^\\d{10,15}$' THEN
            INSERT INTO temp_incorrect_contacts(name, phone, reason)
            VALUES (p_names[i], p_phones[i], 'Phone must contain only digits and length 10-15');
        ELSE
            CALL upsert_contact(p_names[i], p_phones[i]);
        END IF;
    END LOOP;

    OPEN incorrect_data FOR
    SELECT name, phone, reason FROM temp_incorrect_contacts;
END;
$$;

-- 5. Procedure: delete contact by username or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;
