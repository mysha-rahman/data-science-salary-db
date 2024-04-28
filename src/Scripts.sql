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

     -- Filename: create_ds_salaries_table.sql

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