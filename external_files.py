# r = read, w = write, a = append, r+ = read+write
# employee_file = open("employees.txt", "r")

# if employee_file.readable():
#     for employee in employee_file.readlines():
#         print(employee)
# else:
#     print("not readable")
# employee_file.close()

employee_file = open("employees1.txt", "w")

employee_file.write("\nToby - Human Resources")

employee_file.write("\nKelly - Customer Service")
