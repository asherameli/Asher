class Employee():

    def __init__(self,first,last,pay,email):

        self.first=first
        self.last=last
        self.pay=pay
        self.email=email

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1=Employee('corey','shafer',50000,'corey@company.com')
emp_2=Employee('test','user',60000,'user@ucompany.com')

print emp_1.email
print emp_1.fullname()
print Employee.fullname(emp_2)



