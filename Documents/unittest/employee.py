class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

if __name__ == '__main__':
    emp = Employee('mohamed','atif', 3)
    print(emp.email)
    print(emp.__dict__)
