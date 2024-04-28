# Data Science Salaries Management System

## Introduction
Welcome to the Data Science Salaries Management System, a robust database management application designed to handle, query, and manipulate data related to salaries within the data science profession. This project was inspired by the comprehensive [Data Science Salaries Dataset](https://www.kaggle.com/datasets/zain280/data-science-salaries/data) available on Kaggle, which features detailed compensation information across various sectors, geographical locations, and professional levels.

My system is built on PostgreSQL, utilizing advanced database design and SQL scripting to ensure efficient data handling and retrieval. The system is interfaced through a Python-based Command Line Interface (CLI), providing a user-friendly method for performing database operations such as adding, deleting, updating, and querying salary records.

## Project Overview
The Data Science Salaries Management System serves multiple purposes:
- **Data Entry and Management**: Users can add new salary entries, update existing data, or remove salary records, facilitating dynamic data management.
- **Data Analysis**: The system provides functionalities to query the database for specific data insights, such as sorting salaries, grouping employees by experience, and generating reports based on job titles or salary statistics.
- **Data Integration**: Demonstrates seamless integration between a PostgreSQL backend and a Python frontend, illustrating practical database application development.

## Key Features
- **Insertion, Deletion, and Updating of Records**: Directly manipulate the database records through simple CLI commands.
- **Complex Queries Execution**: Perform advanced SQL queries from the CLI, including joins, subqueries, and aggregate functions.
- **Data Integrity and Transaction Management**: Ensures data consistency and integrity with PostgreSQL transaction controls.
- **User-Friendly Interface**: Provides a straightforward command-line interface that guides users through various database operations without needing SQL knowledge.

## Technologies Used
- **PostgreSQL**: For database management, chosen for its robustness, reliability, and suitability for handling complex queries and large datasets.
- **Python**: Used to create the CLI interface, leveraging libraries such as `psycopg2` for database connectivity.
- **CSV Data Import**: Ability to populate the database initially using CSV files, demonstrating data migration and batch processing capabilities.

## Target Audience
This system is intended for a wide range of users, including:
- **Data Scientists** and **Analysts** looking to understand salary trends and variances within their industry.
- **HR Professionals** and **Recruiters** who need a tool to manage and analyze compensation data effectively.
- **Academic Researchers** and **Students** in data science or related fields who require a practical demonstration of database management in action.
- **Policy Makers** and **Economic Analysts** interested in labor market trends and compensation analysis.

## Installation

This section guides you through setting up the Data Science Salaries Management System on your local machine. This setup assumes that you have administrative access to your system and the necessary rights to install software and manage databases.

### Prerequisites
1. **PostgreSQL**: You need PostgreSQL installed on your computer. You can download it from [the official PostgreSQL website](https://www.postgresql.org/download/). Ensure that you remember the credentials for the PostgreSQL superuser (usually `postgres`), as you'll need them to create databases and execute SQL scripts.
2. **Python**: This project requires Python. It's recommended to use Python 3.8 or higher. You can download it from [the official Python website](https://www.python.org/downloads/).
3. **psycopg2**: This Python library is required for PostgreSQL database interaction. Install it via pip:
   ```bash
   pip install psycopg2
   ```
4. **Git**: To clone the repository, make sure you have Git installed. You can download it from [the Git website](https://git-scm.com/downloads).

### Database Setup
#### Creating the Database Tables
1. **Clone the Repository**:
   - First, clone the repository to your local machine
   - The 'data' folder contains all three necessary CSV files for the database, and the 'src' folder includes the Python and SQL code needed for the project.

2. **Run SQL Scripts**:
   - Open your PostgreSQL command line tool (e.g., psql, pgAdmin SQL shell) and connect to your PostgreSQL server.
   - Execute the SQL scripts to create the necessary tables. These scripts can be found in the `src` directory of the cloned repository in 'Scripts' or create them as follows:

     ```sql
     -- Create Employees Table
     CREATE TABLE Employees (
         dsid INT PRIMARY KEY,
         employee_residence VARCHAR(2),
         remote_ratio INT,
         employment_type VARCHAR(50),
         company_location VARCHAR(2),
         company_size VARCHAR(1)
     );

     -- Create JobSalaries Table
     CREATE TABLE JobSalaries (
         dsid INT PRIMARY KEY,
         job_title VARCHAR(255),
         experience_level VARCHAR(50),
         work_year VARCHAR(4),
         salary NUMERIC(12, 2),
         salary_currency VARCHAR(3),
         salary_in_usd NUMERIC(12, 2),
         FOREIGN KEY (dsid) REFERENCES Employees(dsid)
     );

     -- Create DataScienceSalaries Table
     CREATE TABLE DataScienceSalaries (
         dsid INT PRIMARY KEY,
         work_year INT,
         experience_level VARCHAR(2),
         employment_type VARCHAR(2),
         job_title VARCHAR(255),
         salary INT,
         salary_currency VARCHAR(3),
         salary_in_usd INT,
         employee_residence VARCHAR(2),
         remote_ratio INT,
         company_location VARCHAR(2),
         company_size VARCHAR(1)
     );
     ```

#### Importing Data
3. **Load Data into the Tables**:
   - Open pgAdmin and navigate to the respective database.
   - For each table (`Employees`, `JobSalaries`, `DataScienceSalaries`), follow these steps:
     - Right-click on the table.
     - Navigate to the import tool usually found under Tools > Import.
     - Choose the corresponding CSV file from the `data` folder in the cloned repository.
     - Make sure to set the format as CSV and match the columns correctly.
     - Execute the import for each table.

### Running the Application
4. **Execute the Python Script**:
## Python Application Setup

Before running the `DS_Salaries_PyCode.py` script, you need to ensure that your Python environment is properly configured and that the script is set up to connect to your local PostgreSQL server.

### Configuring the Database Connection

The Python script uses `psycopg2` to connect to the PostgreSQL database. You will need to modify the database connection settings in the script to match your PostgreSQL credentials and server details. Follow these steps to update the connection settings:

1. **Open the `DS_Salaries_PyCode.py` file**:
   - Navigate to the `src` directory where `DS_Salaries_PyCode.py` is located.
   - Open the file in a text editor or an IDE of your choice (such as VS Code).

2. **Locate the Database Connection Section**:
   - Find the section in the script where the database connection is set up. It will look something like this:
     ```python
     host_name = "localhost"
     db_user = "postgres"
     db_password = "your_password"
     db_name = "postgres"
     ```
   - Replace `"localhost"`, `"postgres"`, and `"your_password"` with your PostgreSQL server's host name, user name, and password, respectively.
   - If you have created a specific database for this project, replace `"postgres"` with the name of your database.

## Below are descriptions of each function in the provided code:

1. `table_insert(table, data, columns=None)`: Inserts a new record into the specified table with the given data. Optionally, you can specify the columns if you want to insert data into specific columns only.

2. `table_delete(table, id)`: Deletes a record from the specified table based on the provided ID.

3. `table_update(table, id, column, new_value)`: Updates a specific column of a record in the specified table with a new value, based on the provided ID.

4. `insert_employee_entry()`: Prompts the user to enter data for a new employee entry, validates the input, converts it to the appropriate data types, and inserts it into the `employees` table.

5. `delete_employee_entry()`: Prompts the user to enter the ID of the employee to be deleted and then deletes the corresponding records from both the `JobSalaries` and `Employees` tables.

6. `update_employee_salary()`: Prompts the user to enter the ID of the employee and the new salary details, then updates the salary information for the specified employee in the `jobsalaries` table.

7. `search_employee_entry()`: Prompts the user to enter the ID of the employee to search for and retrieves and prints the employee's information if found.

8. `count_employment_type_entry()`: Prompts the user to enter an employment type, counts the number of employees with that type, and prints the count.

9. `sort_employee_salary()`: Retrieves the first 1000 employee entries joined with their salary information from the `employees` and `JobSalaries` tables, sorted by salary in descending order, and prints them.

10. `join_employee_salary_entry()`: Retrieves the first 1000 employee entries joined with their salary information from the `employees` and `JobSalaries` tables, sorted by salary in descending order, and prints them.

11. `group_employee_entry()`: Groups employees by experience level, counts the number of employees in each group, and prints the results.

12. `subquery_employee_entry()`: Prompts the user to enter a job title, retrieves and prints employee information for employees with that job title, limited to 1000 entries.

13. `transaction_delete_employee()`: Prompts the user to enter the ID of the employee to be deleted, starts a transaction, deletes the employee's records from both the `JobSalaries` and `Employees` tables, and commits the transaction if successful.

14. `populate_employee_data_from_csv()`: Reads data from a CSV file containing employee information, skips the header row, and populates the `employees` table with the data.

15. `stateStart()`: Main function that presents a menu to the user, prompts for input, and calls the corresponding function based on the user's choice.

### Common Issues and Troubleshooting
- **PostgreSQL Connection Issues**: Ensure that PostgreSQL is running and your credentials are correct.
- **Python or Library Not Found**: Verify that Python and all required libraries (`psycopg2`) are correctly installed and available in your system's PATH.
