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

    def transfer(self, from_account_id, to_account_id, amount):
        #TODO implement
        # 1. find both accounts
        # 2. perform charge and deposit
        pass

    def find_account(self, acc_id):
        #TODO loop through the list of accounts and return the matching account
        pass

    def __repr__(self):
        return f'Bank:\n{self.customer_list}\n{self.account_list}\n----------'


#c1 = Customer('John', "Smith")
b = Bank()
c1 = b.create_customer('John', 'Smith')
print(c1)
print(b)
a1 = b.create_account(c1)
#a = Account(c1)
print(a1)
a1.deposit(100)
print(a1)
a1.charge(50)
print(a1)
a2 = b.create_account(c1)
print('Before transfer')
print(b)
b.transfer(1001, 1002, 20)
print('After transfer')
print(b)
