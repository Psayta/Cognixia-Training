# Code used to input new employees into a list with their name, age and email 
employee_list = [] #Empty list of employees 
while True: #begins loop 
    try:
        employees = int(input('How many employees: ')) #input for number of employees
    except ValueError: #exception handle for non int values 
        print("You did not enter a number")
    else: 
        print(f'{employees} Employees accepted')#returns string indicating that the int is accepted 
        break #stops 

for n in range (employees): #for loop uses the number of employees indicated from previous input
    employee_record = { "name" : '', "age" : 0, "email": ''} #creating a set for employees with keys
    name = input('Enter first and last name w/space: ').split(' ') #inputs for names that are split between first and last 
    employee_record["name"] = name #passes names inputted into the set 
            
    try: 
        age = int(input('Enter your age: '))#input for age 
        employee_record["age"] = age #places int for age in employee record
        if (age < 18): raise ValueError #exception handle for ages to young to work 
    except ValueError: 
        print('Employee too young')#indicator for the value error that employee is to young
        
    employee_record["email"]  = name[0] + "." + name[1] + '@company.com' #concatanate to create employee email 
    employee_list.append(employee_record) #adds each employee record in the set to the employee_list 

print (employee_list) #prints the new employee list with addes records from employee_record

