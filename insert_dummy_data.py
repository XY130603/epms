import os
import pymysql
from datetime import datetime

# Database connection (connect to MySQL server, not the specific database)
con = pymysql.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="Paul@130603"  # Replace with your MySQL password
)

try:
    with con.cursor() as cur:
        # Check if the 'ems' database exists
        cur.execute("SHOW DATABASES LIKE 'ems';")
        db_exists = cur.fetchone()

        if db_exists:
            # Switch to the 'ems' database and truncate the table
            cur.execute("USE ems;")
            cur.execute("TRUNCATE TABLE emp_salary;")  # Clears all data and resets auto-increment
            print("Existing data in 'emp_salary' table cleared.")
        else:
            # Create the 'ems' database and table if they don't exist
            cur.execute("CREATE DATABASE IF NOT EXISTS ems;")
            cur.execute("USE ems;")
            cur.execute("""
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
            """)
            print("'ems' database and 'emp_salary' table created.")

    # Commit changes
    con.commit()

except Exception as ex:
    print(f"Error: {ex}")
finally:
    con.close()

# Reconnect to the 'ems' database to insert dummy data
con = pymysql.connect(
    host="localhost",
    user="root",
    password="Paul@130603",
    database="ems"
)

# Dummy data (10 entries)
dummy_employees = [
    {
        'e_id': 'E001',
        'designation': 'Manager',
        'name': 'Alice Johnson',
        'age': '30',
        'gender': 'Female',
        'email': 'alice@example.com',
        'hr_location': 'New York',
        'dob': '1990-05-15',
        'doj': '2015-06-01',
        'experience': '8 years',
        'proof_id': 'A123456789',
        'contact': '5551234567',
        'status': 'Active',
        'address': '123 Main St, New York',
        'month': 'January',
        'year': '2023',
        'basic_salary': 8000.00,
        't_days': 22,
        'absent_days': 2,
        'medical': 500.00,
        'pf': 1000.00,
        'conveyance': 300.00,
        'net_salary': 7800.00,
        'salary_receipt': 'E001.txt'
    },
    {
        'e_id': 'E002',
        'designation': 'Developer',
        'name': 'Bob Brown',
        'age': '25',
        'gender': 'Male',
        'email': 'bob@example.com',
        'hr_location': 'San Francisco',
        'dob': '1998-08-20',
        'doj': '2020-07-15',
        'experience': '3 years',
        'proof_id': 'B987654321',
        'contact': '5559876543',
        'status': 'Active',
        'address': '456 Elm St, San Francisco',
        'month': 'February',
        'year': '2023',
        'basic_salary': 6000.00,
        't_days': 20,
        'absent_days': 1,
        'medical': 300.00,
        'pf': 800.00,
        'conveyance': 200.00,
        'net_salary': 6200.00,
        'salary_receipt': 'E002.txt'
    },
    # Add 8 more entries
    {
        'e_id': 'E003',
        'designation': 'Accountant',
        'name': 'Charlie Davis',
        'age': '28',
        'gender': 'Male',
        'email': 'charlie@example.com',
        'hr_location': 'London',
        'dob': '1995-03-25',
        'doj': '2018-09-10',
        'experience': '5 years',
        'proof_id': 'C123456789',
        'contact': '5551122334',
        'status': 'Active',
        'address': '789 Oak St, London',
        'month': 'March',
        'year': '2023',
        'basic_salary': 5500.00,
        't_days': 22,
        'absent_days': 3,
        'medical': 400.00,
        'pf': 700.00,
        'conveyance': 250.00,
        'net_salary': 5500 - (5500/22)*3 - 400 - 700 + 250,
        'salary_receipt': 'E003.txt'
    },
    {
        'e_id': 'E004',
        'designation': 'HR Manager',
        'name': 'Eva Wilson',
        'age': '32',
        'gender': 'Female',
        'email': 'eva@example.com',
        'hr_location': 'Chicago',
        'dob': '1991-12-05',
        'doj': '2016-02-20',
        'experience': '7 years',
        'proof_id': 'E456789123',
        'contact': '5554443322',
        'status': 'Active',
        'address': '101 Pine St, Chicago',
        'month': 'April',
        'year': '2023',
        'basic_salary': 7000.00,
        't_days': 22,
        'absent_days': 1,
        'medical': 600.00,
        'pf': 900.00,
        'conveyance': 350.00,
        'net_salary': 7000 - (7000/22)*1 - 600 - 900 + 350,
        'salary_receipt': 'E004.txt'
    },
    {
        'e_id': 'E005',
        'designation': 'Sales Executive',
        'name': 'Frank Miller',
        'age': '27',
        'gender': 'Male',
        'email': 'frank@example.com',
        'hr_location': 'Los Angeles',
        'dob': '1996-07-12',
        'doj': '2021-05-01',
        'experience': '2 years',
        'proof_id': 'F789123456',
        'contact': '5557778899',
        'status': 'Inactive',
        'address': '202 Maple St, LA',
        'month': 'May',
        'year': '2023',
        'basic_salary': 4500.00,
        't_days': 22,
        'absent_days': 4,
        'medical': 200.00,
        'pf': 500.00,
        'conveyance': 150.00,
        'net_salary': 4500 - (4500/22)*4 - 200 - 500 + 150,
        'salary_receipt': 'E005.txt'
    },
    {
        'e_id': 'E006',
        'designation': 'Data Analyst',
        'name': 'Grace Lee',
        'age': '29',
        'gender': 'Female',
        'email': 'grace@example.com',
        'hr_location': 'Boston',
        'dob': '1994-04-18',
        'doj': '2019-11-30',
        'experience': '4 years',
        'proof_id': 'G321654987',
        'contact': '5553334455',
        'status': 'Active',
        'address': '303 Cedar St, Boston',
        'month': 'June',
        'year': '2023',
        'basic_salary': 6500.00,
        't_days': 22,
        'absent_days': 0,
        'medical': 450.00,
        'pf': 800.00,
        'conveyance': 300.00,
        'net_salary': 6500 - (6500/22)*0 - 450 - 800 + 300,
        'salary_receipt': 'E006.txt'
    },
    {
        'e_id': 'E007',
        'designation': 'Marketing Lead',
        'name': 'Henry Clark',
        'age': '31',
        'gender': 'Male',
        'email': 'henry@example.com',
        'hr_location': 'Austin',
        'dob': '1992-09-22',
        'doj': '2017-08-14',
        'experience': '6 years',
        'proof_id': 'H987654321',
        'contact': '5556667788',
        'status': 'Active',
        'address': '404 Birch St, Austin',
        'month': 'July',
        'year': '2023',
        'basic_salary': 7200.00,
        't_days': 22,
        'absent_days': 2,
        'medical': 550.00,
        'pf': 950.00,
        'conveyance': 400.00,
        'net_salary': 7200 - (7200/22)*2 - 550 - 950 + 400,
        'salary_receipt': 'E007.txt'
    },
    {
        'e_id': 'E008',
        'designation': 'UI Designer',
        'name': 'Ivy White',
        'age': '26',
        'gender': 'Female',
        'email': 'ivy@example.com',
        'hr_location': 'Seattle',
        'dob': '1997-11-30',
        'doj': '2022-01-10',
        'experience': '1 year',
        'proof_id': 'I123789456',
        'contact': '5551112233',
        'status': 'Active',
        'address': '505 Walnut St, Seattle',
        'month': 'August',
        'year': '2023',
        'basic_salary': 5000.00,
        't_days': 22,
        'absent_days': 3,
        'medical': 300.00,
        'pf': 600.00,
        'conveyance': 200.00,
        'net_salary': 5000 - (5000/22)*3 - 300 - 600 + 200,
        'salary_receipt': 'E008.txt'
    },
    {
        'e_id': 'E009',
        'designation': 'QA Engineer',
        'name': 'Jack Harris',
        'age': '33',
        'gender': 'Male',
        'email': 'jack@example.com',
        'hr_location': 'Denver',
        'dob': '1990-02-14',
        'doj': '2014-04-22',
        'experience': '9 years',
        'proof_id': 'J789456123',
        'contact': '5559998877',
        'status': 'Active',
        'address': '606 Oak St, Denver',
        'month': 'September',
        'year': '2023',
        'basic_salary': 7500.00,
        't_days': 22,
        'absent_days': 1,
        'medical': 600.00,
        'pf': 1000.00,
        'conveyance': 450.00,
        'net_salary': 7500 - (7500/22)*1 - 600 - 1000 + 450,
        'salary_receipt': 'E009.txt'
    },
    {
        'e_id': 'E010',
        'designation': 'Project Manager',
        'name': 'Karen Smith',
        'age': '35',
        'gender': 'Female',
        'email': 'karen@example.com',
        'hr_location': 'Miami',
        'dob': '1988-10-08',
        'doj': '2012-12-01',
        'experience': '11 years',
        'proof_id': 'K456123789',
        'contact': '5554445566',
        'status': 'Inactive',
        'address': '707 Palm St, Miami',
        'month': 'October',
        'year': '2023',
        'basic_salary': 8500.00,
        't_days': 22,
        'absent_days': 5,
        'medical': 700.00,
        'pf': 1200.00,
        'conveyance': 500.00,
        'net_salary': 8500 - (8500/22)*5 - 700 - 1200 + 500,
        'salary_receipt': 'E010.txt'
    }
]

try:
    with con.cursor() as cur:
        for emp in dummy_employees:
            # Calculate net salary dynamically
            per_day = emp['basic_salary'] / emp['t_days']
            work_days = emp['t_days'] - emp['absent_days']
            net_salary = per_day * work_days - emp['medical'] - emp['pf'] + emp['conveyance']
            emp['net_salary'] = round(net_salary, 2)
            
            # Insert into emp_salary
            cur.execute("""
                INSERT INTO emp_salary VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                emp['e_id'], emp['designation'], emp['name'], emp['age'], emp['gender'], emp['email'], emp['hr_location'], emp['dob'], emp['doj'], emp['experience'], emp['proof_id'], emp['contact'], emp['status'], emp['address'], emp['month'], emp['year'], emp['basic_salary'], emp['t_days'], emp['absent_days'], emp['medical'], emp['pf'], emp['conveyance'], emp['net_salary'], emp['salary_receipt']
            ))
        con.commit()
        print("10 dummy employees added to the 'ems' database.")
finally:
    con.close()

# Create receipts directory if missing
os.makedirs('receipts', exist_ok=True)

# Add this code after inserting each employee into the database
for emp in dummy_employees:
    # Generate receipt content
    receipt_content = f"""Company Name: Darkrose INC
Address: A.P,India
--------------------------------------------------------
 Employee ID\t\t: {emp['e_id']}
 Salary of\t\t: {emp['month']}-{emp['year']}
 Generated on\t\t: {datetime.now().strftime("%d-%m-%Y")}
--------------------------------------------------------
 Total Days\t\t: {emp['t_days']}
 Total Present\t\t: {emp['t_days'] - emp['absent_days']}
 Total Absent\t\t: {emp['absent_days']}
 Conveyance\t\t: Rs.{emp['conveyance']}
 Medical\t\t: Rs.{emp['medical']}
 PF\t\t: Rs.{emp['pf']}
 Gross Payment\t\t: Rs{emp['basic_salary']}
 Net Salary\t\t: Rs.{emp['net_salary']}
-------------------------------------------------------
This is Computer Generated slip,\tSignature not required"""

    # Save the receipt file
    os.makedirs('receipts', exist_ok=True)
    file_path = os.path.join('receipts', f"{emp['e_id']}.txt")
    with open(file_path, 'w') as f:
        f.write(receipt_content)