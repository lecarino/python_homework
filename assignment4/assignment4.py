# TO TEST: pytest -v -x assignment4-test.py.
import pandas as pd

'''Task 1: Introduction to Pandas - Creating and Manipulating DataFrames'''

# 1. Create a DataFrame from a dictionary:
data = {
    'Name': ['Alice','Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary into a DataFrame using Pandas.
task1_data_frame = pd.DataFrame(data)

# Print Dataframe
print(task1_data_frame)


# 2. Add a new column:
# Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
task1_with_salary =  task1_data_frame.copy()

# Add a column called Salary with values [70000, 80000, 90000].
Salary = [70000, 80000, 90000]
task1_with_salary['Salary'] = Salary

print(task1_with_salary)

# 3. Modify an existing column
# Make a copy of task1_with_salary in a variable named task1_older
task1_older = task1_with_salary.copy()

# Increment the Age column by 1 for each entry.
task1_older['Age'] = task1_older['Age']+1
print(task1_older)

# 4. Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)

'''Task 2: Loading Data from CSV and JSON'''
# 1. Read data from a CSV file:
task2_employees = pd.read_csv("employees.csv")
print("\nTASK2.1:\n")
print(task2_employees)

# 2. Read data from a JSON:
json_employees = pd.read_json("additional_employees.json")
print("\nTASK2.2:\n")
print(json_employees)

# 3. Combine DataFrames:
# Combine the data from the JSON file into the DataFrame Loaded from the CSV file
more_employees = pd.concat([task2_employees,json_employees], ignore_index=True)
print("\nTASK2.3:\n")
print(more_employees)

'''Task 3: Data Inspection - Using Head, Tail, and Info Methods'''
# 1. Use the head() method:
# Assign the first three rows of the more_employees DataFrame to the variable first_three
print("\nTASK3.1:\n")
first_three = more_employees.head(3)
print(first_three)

# 2. Use the tail() method:
print("\nTASK3.2:\n")
last_two = more_employees.tail(2)
print(last_two)

# 3. Get the shape of a DataFrame
print("\nTASK3.3:\n")
employee_shape = more_employees.shape
print(employee_shape)

# 4. info()
print("\nTASK3.4:\n")
print(more_employees.info())

'''Task 4: Data Cleaning'''
# 1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv('dirty_data.csv')
print("\n Task4.1 \n")
print(dirty_data)

# clean_data
clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print("\n Task4.2 \n")
print(clean_data)

# 3. Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\n Task4.3 \n")
print(clean_data)

# 4. Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = clean_data["Salary"].replace("Unknown", pd.NA).fillna("NaN")
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\n Task4.4 \n")
print(clean_data)

# 5. Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data["Age"].mean()
median_salary = clean_data["Salary"].median()

clean_data["Age"] = clean_data["Age"].fillna(mean_age)
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print("\n Task4.5 \n")
print(clean_data)

# 6. Convert Hire Date to datetime
clean_data["Hire Date"]= pd.to_datetime(clean_data["Hire Date"], format="mixed")
print("\n Task4.6 \n")
print(clean_data)

# 7 Strip extra whitespace and standardize Name and Department as uppercase
# Strip
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip()

# Upper
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.upper()
print(clean_data)