# Task 3: List Comprehensions Practice
import csv

try:
    with open("../csv/employees.csv","r") as file:
        reader = csv.reader(file)
        employee_names =[f"{line[1]}  {line[2]}" for index, line in enumerate(reader) if index > 0]

except Exception as e:
    print(e)

print(employee_names)
names_with_e_only = [name for name in employee_names if "e" in name]
print(f"here are the names with e only: {names_with_e_only}")