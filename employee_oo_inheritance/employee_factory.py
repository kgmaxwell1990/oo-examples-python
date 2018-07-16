from employee.employee import Employee, Developer, SalesPerson

employee_1 = Employee('joe', 'bloggs', 2)
employee_2 = Employee('tom', 'smith', 5)
employee_3 = Employee('alice', 'jones', 6)

print(employee_1.get_details())
print(employee_2.get_details())
print(employee_3.get_details() + "\n")


developer_1 = Developer('tim', 'brown', 2, 'python')
developer_2 = Developer('joe', 'smith', 5, 'Javascript')
developer_3 = Developer('bob', 'brown', 6, 'HTML')

print(developer_1.get_details())
print(developer_2.get_details())
print(developer_3.get_details() + "\n")

sales_1 = SalesPerson('tim', 'brown', 2, 'uk')
sales_2 = SalesPerson('joe', 'smith', 5, 'ireland')
sales_3 = SalesPerson('bob', 'brown', 6, 'europe')

print(sales_1.get_details())
print(sales_2.get_details())
print(sales_3.get_details())
