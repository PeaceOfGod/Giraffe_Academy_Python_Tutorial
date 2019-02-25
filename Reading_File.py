Employee_File = open("Employee.txt", "r")
for employee in Employee_File.readlines():
    print(employee)
#print(Employee_File.readline())
Employee_File.close()