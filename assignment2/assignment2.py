#Task 2: Read a CSV File
import csv
#Create a function called read_employees that has no arguments, and do the following within it
def read_employees():
    emp_dict = {}
    rows_list = []

    #You next read a csv file. Use a try block and a with statement, so that your code is robust and so that the file gets closed.
    try:
        with open("../csv/employees.csv",'r') as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader):
                if index == 0:
                   emp_dict['fields'] = row
                else:
                   rows_list.append(row)
            emp_dict['rows'] = rows_list
            return emp_dict
    except Exception as e:
        print(e)
employees = read_employees()
print(employees)