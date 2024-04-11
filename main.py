# AttributeError: can't set attribute in Python

from collections import namedtuple

EmployeeRecord = namedtuple(
    'EmployeeRecord',
    ['name', 'age', 'salary']
)

emp1 = EmployeeRecord('Bobby Hadz', 30, 1500)

# 👇️ EmployeeRecord(name='Bobby Hadz', age=30, salary=1500)
print(emp1)

emp1 = emp1._replace(salary=2000)
print(emp1)

print(emp1[2])  # 👉️ 2000
print(emp1.salary)  # 👉️ 2000