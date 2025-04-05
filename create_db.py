import mysql.connector
from mysql.connector import Error

# Define the SQL commands as a string
sql_commands = """
-- Create the registration database
CREATE DATABASE IF NOT EXISTS registration;

-- Use the registration database
USE registration;

-- Create the user registration table
CREATE TABLE IF NOT EXISTS regfields (
    id INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(100) NOT NULL,
    l_name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100) UNIQUE NOT NULL,
    question VARCHAR(100) NOT NULL,
    answer VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Create the ems database
CREATE DATABASE IF NOT EXISTS ems;

-- Use the ems database
USE ems;

-- Create the employee salary table
CREATE TABLE IF NOT EXISTS emp_salary (
    e_id VARCHAR(20) PRIMARY KEY,
    designation VARCHAR(100),
    name VARCHAR(100) NOT NULL,
    age VARCHAR(10),
    gender VARCHAR(10),
    email VARCHAR(100) NOT NULL,
    hr_location VARCHAR(100),
    dob VARCHAR(20),
    doj VARCHAR(20),
    experience VARCHAR(50),
    proof_id VARCHAR(100),
    contact VARCHAR(20),
    status VARCHAR(20),
    address TEXT,
    month VARCHAR(20),
    year VARCHAR(10),
    basic_salary DECIMAL(12,2),
    t_days INT,
    absent_days INT,
    medical DECIMAL(10,2),
    pf DECIMAL(10,2),
    conveyance DECIMAL(10,2),
    net_salary DECIMAL(12,2),
    salary_receipt VARCHAR(100)
);
"""

def create_database_and_tables():
    connection = None  # Initialize connection as None
    try:
        # Connect to MySQL server (replace with your credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="Paul130603",  # Replace with your MySQL username
            password="Paul@130603"  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Split the SQL commands into individual statements
            commands = sql_commands.split(";")

            # Execute each command
            for command in commands:
                command = command.strip()
                if command:  # Ignore empty commands
                    cursor.execute(command)

            print("Database and tables created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure connection is closed even if an exception occurs
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Call the function to execute the SQL commands
create_database_and_tables()