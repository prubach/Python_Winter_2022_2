class Customer:
    last_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f"Customer id: {self.id} {self.firstname} {self.lastname}"



class Account:
    last_id = 1000
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def charge(self, amount):
        self._balance -= amount

    def __repr__(self):
        return f'Account [{self.id}, {self.customer.lastname}, {self._balance}]'



c1 = Customer('John', "Smith")
print(c1)

a = Account(c1)
print(a)
a.deposit(100)
print(a)
a.charge(50)
print(a)