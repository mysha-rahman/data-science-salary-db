# Data Science Salaries Management System

## Introduction
Welcome to the Data Science Salaries Management System, a robust database management application designed to handle, query, and manipulate data related to salaries within the data science profession. This project was inspired by the comprehensive [Data Science Salaries Dataset](https://www.kaggle.com/datasets/zain280/data-science-salaries/data) available on Kaggle, which features detailed compensation information across various sectors, geographical locations, and professional levels.

Our system is built on PostgreSQL, utilizing advanced database design and SQL scripting to ensure efficient data handling and retrieval. The system is interfaced through a Python-based Command Line Interface (CLI), providing a user-friendly method for performing database operations such as adding, deleting, updating, and querying salary records.

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

