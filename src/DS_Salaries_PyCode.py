import psycopg2 as db_connect
import csv
from io import StringIO

host_name="localhost"
db_user="postgres"
db_password="Mysha2050"
db_name="postgres"

NUM_COLUMNS = 12

connection = db_connect.connect(host=host_name,user=db_user,password=db_password,database=db_name)
cursor = connection.cursor()

def table_insert(table, data):
    formatted_values = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table} VALUES ({formatted_values})"
    cursor.execute(query, data)

def table_delete(table, id):
    query = f"DELETE FROM {table} WHERE dsid = '{id}';"
    cursor.execute(query)

def table_update(table, id, column, newVal):
    query = f"UPDATE {table} SET {column} = '{newVal}' WHERE dsid = '{id}';"
    cursor.execute(query)

def insert_employee_entry():
    dsid = input("Enter the Data Science ID (dsid): ")
    attributes = input("Enter the following attributes separated by a comma and space: "
                       "work_year, experience_level, employment_type, job_title, salary, "
                       "salary_currency, salary_in_usd, employee_residence, remote_ratio, "
                       "company_location, company_size: ")
    attributeList = attributes.split(", ")
    if (len(attributeList) != 11):
        print("Invalid amount of entries! Expected 11 entries.")
    else:
        employee_data = (int(dsid), attributeList[0], attributeList[1], attributeList[2], attributeList[3], float(attributeList[4]),
                         attributeList[5], float(attributeList[6]), attributeList[7], int(attributeList[8]),
                         attributeList[9], attributeList[10])
        try:
            table_insert('employees', employee_data)
            print("Employee entry successfully added.")
        except Exception as e:
            print(f"Error inserting data: {e}")
        connection.commit()

def table_insert(table, data):
    placeholders = ', '.join(['%s'] * len(data))
    columns = '(dsid, work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd, employee_residence, remote_ratio, company_location, company_size)'
    query = f"INSERT INTO {table} {columns} VALUES ({placeholders})"
    cursor.execute(query, data)

def delete_employee_entry():
    employee_id = input("Enter the Employee ID (dsid) to delete: ")
    try:
        table_delete('JobSalaries', employee_id)
        table_delete('Employees', employee_id)
        print("Employee entry successfully deleted.")
        connection.commit()
    except Exception as e:
        print(f"Error deleting data: {e}")
        connection.rollback()  

def update_employee_salary():
    employee_id = input("Enter the Employee ID (dsid) for salary update: ")
    new_salary = input("Enter the new salary amount: ")
    new_salary_in_usd = input("Enter the new salary amount in USD: ")
    try:
        table_update('jobsalaries', employee_id, new_salary, new_salary_in_usd)
        print("Employee salary successfully updated.")
    except Exception as e:
        print(f"Error updating data: {e}")
    connection.commit()

def table_delete(table, employee_id):
    query = f"DELETE FROM {table} WHERE dsid = %s;"
    cursor.execute(query, (employee_id,))

def table_update(table, employee_id, new_salary, new_salary_in_usd):
    query = f"UPDATE {table} SET salary = %s, salary_in_usd = %s WHERE dsid = %s;"
    cursor.execute(query, (new_salary, new_salary_in_usd, employee_id))

# Search existing employee entry in the database
def search_employee_entry():
    dsid = input("Enter the Employee ID (dsid) to search: ")
    try:
        query = f"SELECT * FROM Employees WHERE dsid = %s;"
        cursor.execute(query, (dsid,))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No employee found with that ID.")
    except Exception as e:
        print(f"Error selecting data: {e}")

# Count employees based on employment type in the database
def count_employment_type_entry():
    employment_type = input("Enter the Employment Type to count (e.g., 'FT' for Full-Time, 'PT' for Part-Time): ")
    try:
        query = f"SELECT COUNT(*) FROM Employees WHERE employment_type = %s;"
        cursor.execute(query, (employment_type,))
        results = cursor.fetchall()
        print(f"Count of {employment_type}: {results[0][0]}")
    except Exception as e:
        print(f"Error selecting data: {e}")

# Sort employee entries in the database by salary
def sort_employee_salary():
    try:
        query = "SELECT * FROM Employees JOIN JobSalaries ON Employees.dsid = JobSalaries.dsid ORDER BY salary_in_usd DESC LIMIT 1000;"
        cursor.execute(query)
        results = cursor.fetchall()
        print("First 1000 entries sorted by Salary in USD (Descending):")
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error selecting data: {e}")

def join_employee_salary_entry():
    try:
        query = """SELECT e.dsid, e.employee_residence, e.remote_ratio, e.employment_type, e.company_location, e.company_size,
                   js.job_title, js.experience_level, js.work_year, js.salary, js.salary_currency, js.salary_in_usd
                   FROM Employees e
                   INNER JOIN JobSalaries js
                   ON e.dsid = js.dsid
                   ORDER BY js.salary_in_usd DESC LIMIT 1000;"""
        cursor.execute(query)
        results = cursor.fetchall()
        print("First 1000 entries joined by Employee ID, sorted by Salary in USD (Descending):")
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error selecting data: {e}")

def group_employee_entry():
    try:
        query = """
        SELECT js.experience_level, COUNT(e.dsid) 
        FROM Employees e 
        JOIN JobSalaries js ON e.dsid = js.dsid 
        GROUP BY js.experience_level;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print("Grouping Employees by Experience Level:")
        for row in results:
            print(f"Experience Level: {row[0]} | Number of Employees: {row[1]}")
    except Exception as e:
        print(f"Error selecting data: {e}")

def subquery_employee_entry():
    job_title = input("Enter the Job Title to search for: ")
    try:
        print(f"Selecting employees with Job Title: {job_title}")
        query = f"""
        SELECT e.* FROM Employees e
        WHERE e.dsid IN (
            SELECT js.dsid FROM JobSalaries js
            WHERE js.job_title = %s
        ) LIMIT 1000;
        """
        cursor.execute(query, (job_title,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error selecting data: {e}")

def transaction_delete_employee():
    employee_id = input("Enter the Employee ID (dsid) to delete: ")
    try:
        connection.autocommit = False
        print("Transaction started.")
        table_delete('JobSalaries', employee_id)
        table_delete('Employees', employee_id)
        connection.commit()
        print("Transaction committed.")
    except Exception as e:
        connection.rollback()
        print(f"Error during transaction, changes rolled back: {e}")
    finally:
        connection.autocommit = True

def populate_employee_data_from_csv():
    filename = r'C:\Users\mysha\OneDrive\Desktop\CS 431W\Stage 2\ds_salaries.csv' 
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            # Assuming the connection and cursor are already established
            cursor.copy_from(csvfile, 'employees', sep=',')
            print("Employee data populated successfully from CSV.")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error populating employee data from CSV: {e}")

def stateStart():
    userInput = 0
    print("----------------------------------------------------------")
    print("Welcome to the Data Science Salaries Management Interface!")
    print("----------------------------------------------------------\n")
    print("Please select an option:\n")
    print("1. Insert New Employee Entry\n2. Delete Employee Entry\n3. Update Employee Salary Entry\n4. Search Employee Entry\n5. Count Employees by Type\n6. Sort Employees by Salary\n7. Join Employee with Salaries\n8. Group Employees by Experience\n9. Subquery Employee by Job Title\n10.Transactions for Employee Deletion\n11.Populate Employee Data from CSV\n12.Exit\n\n")
    userInput = input("Enter your choice (1-12):")
    try:
        userInput = int(userInput)
    except:
        print("Invalid input. Please try again!")
    
    if userInput == 1:
        insert_employee_entry()
    elif userInput == 2:
        delete_employee_entry()
    elif userInput == 3:
        update_employee_salary()
    elif userInput == 4:
        search_employee_entry()
    elif userInput == 5:
        count_employment_type_entry()
    elif userInput == 6:
        sort_employee_salary()
    elif userInput == 7:
        join_employee_salary_entry()
    elif userInput == 8:
        group_employee_entry()
    elif userInput == 9:
        subquery_employee_entry()
    elif userInput == 10:
        transaction_delete_employee()
    elif userInput == 11:
        populate_employee_data_from_csv()
    elif userInput == 12:
        print("Exiting Interface...")

if __name__ == "__main__":
    stateStart()
connection.close()


