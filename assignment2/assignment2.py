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
# print(employees)

#Task 3: Find the Column Index #Finds column_index of a field input
def column_index(str):
    return employees["fields"].index(str)
employee_id_column = column_index("employee_id")
# print(employee_id_column)

''' employees variable:
{   'fields':   ['employee_id', 'first_name', 'last_name', 'phone'], 
    'rows':     [
                    ['1', 'Cindy', 'Wade', '+222 656-486-3727'], 
                    ['2', 'David', 'Thornton', '+882 (369)732-4858x56864'], 
                    ['3', 'Lauren', 'Martinez', '+250 8878764159'], 
                    ['4', 'Kenneth', 'White', '+64 4924992211'], 
                    ['5', 'James', 'Torres', '+267 +1-471-316-0190x308'], 
                    ['6', 'Tracy', 'Foster', '+237 6225761379'], 
                    ['7', 'Miranda', 'Harris', '+370 001-563-522-4308x77248'], 
                    ['8', 'Destiny', 'Nguyen', '+226 284.891.0715'], 
                    ['9', 'Phillip', 'Williams', '+423 4943292679'], 
                    ['10', 'Kelli', 'Bowman', '+379 (843)240-1818x77648'], 
                    ['11', 'Gregory', 'Pittman', '+264 9864625899'], 
                    ['12', 'Natasha', 'Hoover', '+234 649.763.1540x547'], 
                    ['13', 'Gregory', 'Jackson', '+243 (871)628-0556'], 
                    ['14', 'David', 'Clark', '+882 805-740-2877x32513'], 
                    ['15', 'Sarah', 'Shepherd', '+267 721-710-7210x8468'], 
                    ['16', 'Michael', 'Quinn', '+972 826.201.6869'], 
                    ['17', 'Logan', 'Lopez', '+64 +1-264-270-6434'], 
                    ['18', 'Donald', 'Hunt', '+47 79 (579)967-8837x893'], 
                    ['19', 'Matthew', 'Meyers', '+378 +1-720-722-2062x240'], 
                    ['20', 'Thomas', 'Calderon', '+64 +1-380-200-3211']
                ]
}

'''

# Task 4: Find the Employee First Name. The function should retrieve the value of first_name from a row as stored in the employees dict.
def first_name(row):
    fname_idx = column_index('first_name') #You should first call your column_index function to find out what column index you want.
    return employees['rows'][row][fname_idx]
# print(first_name(2))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):        #We want it to return the rows with the matching employee_id.  There should only be one, but sometimes a CSV file has bad data.
    
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))
    ''' 
    The filter() function needs to know how to filter, and the employee_match function provides that information.  
    The filter() function calls employee_match once per row, saying, Do we want this one?  
    When the filter function completes, we need to do type conversion to convert the result to a list.
    '''
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():    #We want to call the sort() method on the rows.  However, we need to tell it which column to use for the sort.
    #index of last name
    idx = column_index('last_name')

    #sort list inside dictionary by index of 'last_name'
    employees["rows"].sort(key=lambda row: row[idx])
    
    #Checking:
    print(employees["rows"])
    '''
    [['10', 'Kelli', 'Bowman', '+379 (843)240-1818x77648'], 
    ['20', 'Thomas', 'Calderon', '+64 +1-380-200-3211'], 
    ['14', 'David', 'Clark', '+882 805-740-2877x32513'], 
    ['6', 'Tracy', 'Foster', '+237 6225761379'], 
    ['7', 'Miranda', 'Harris', '+370 001-563-522-4308x77248'], 
    ['12', 'Natasha', 'Hoover', '+234 649.763.1540x547'], 
    ['18', 'Donald', 'Hunt', '+47 79 (579)967-8837x893'], 
    ['13', 'Gregory', 'Jackson', '+243 (871)628-0556'], 
    ['17', 'Logan', 'Lopez', '+64 +1-264-270-6434'], 
    ['3', 'Lauren', 'Martinez', '+250 8878764159'], 
    ['19', 'Matthew', 'Meyers', '+378 +1-720-722-2062x240'], 
    ['8', 'Destiny', 'Nguyen', '+226 284.891.0715'], 
    ['11', 'Gregory', 'Pittman', '+264 9864625899'], 
    ['16', 'Michael', 'Quinn', '+972 826.201.6869'], 
    ['15', 'Sarah', 'Shepherd', '+267 721-710-7210x8468'], 
    ['2', 'David', 'Thornton', '+882 (369)732-4858x56864'], 
    ['5', 'James', 'Torres', '+267 +1-471-316-0190x308'], 
    ['1', 'Cindy', 'Wade', '+222 656-486-3727'], 
    ['4', 'Kenneth', 'White', '+64 4924992211'], 
    ['9', 'Phillip', 'Williams', '+423 4943292679']]
    '''
    return employees["rows"]

# Task 8: Create a dict for an Employee
def employee_dict(row):
    # The keys in the dict are the column headers from employees["fields"]. Do not include employee_id
    # zip() joins two tuples. zip(fields,desired_row)
    emp_keys = employees["fields"][1:] # No employee_ids
    emp_vals = row[1:] #input is a row not row number!
    # specific emplyee turned into a dictionary
    emp = dict(zip(emp_keys,emp_vals)) 
    return emp

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    # The keys in the dict are the employee_id values from the rows in the employees dict.
    # For each key, the value is the employee dict created for that row. (Use the employee_dict function you created in task 8.)
    emps = {}
    for row in employees["rows"]:   # Loop through each row and separate the keys and the values
        key = row[0]
        emps[key] = employee_dict(row) #use employee dict to get dictionary of employee
    return emps

# Task 10: Use the os Module
import os
def get_this_value():
    #This function takes no parameters and returns the value of the environment variable THISVALUE.
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
import custom_module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("secretsecret")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv