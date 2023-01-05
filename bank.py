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


class Bank:

    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def __repr__(self):
        return f'Bank:\n{self.customer_list}\n{self.account_list}\n----------'


#c1 = Customer('John', "Smith")
b = Bank()
c1 = b.create_customer('John', 'Smith')
print(c1)
print(b)
a = b.create_account(c1)
#a = Account(c1)
print(a)
a.deposit(100)
print(a)
a.charge(50)
print(a)

print(b)