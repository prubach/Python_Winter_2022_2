from sqlalchemy import Column, Integer, String, Float, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(60), nullable=True)
    lastname = Column(String(60), nullable=False)
    email = Column(String(120), nullable=True)



    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return f"Customer id: {self.id} {self.firstname} {self.lastname}"


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, default=0)

    def __init__(self, customer):
        self.customer = customer

    def deposit(self, amount):
        #TODO add throwing exception when amount is invalid
        self.balance += amount

    def charge(self, amount):
        #TODO add throwing exception when amount is invalid or there are insufficient funds
        self.balance -= amount

    def __repr__(self):
        return f'Account [{self.id}, {self.customer.lastname}, {self.balance}]'


class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name
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
        ##TODO implement
        ## 1. find both accounts
        ## 2. perform charge and deposit
        from_acc = self.find_account(from_account_id)
        to_acc = self.find_account(to_account_id)
        from_acc.charge(amount)
        to_acc.deposit(amount)

    def find_account(self, acc_id):
        # loop through the list of accounts and return the matching account
        for acc in self.account_list:
            if acc.id == acc_id:
                return acc
        return None

    def __repr__(self):
        return f'Bank:\n{self.customer_list}\n{self.account_list}\n----------'


class BankException(Exception):
    def __init__(self, msg, amount):
        super().__init__(msg)
        self.amount = amount
# to throw the above BankException you can use the following code:
# raise BankException('Amount is not valid', amount)

class DBSession:
    current_db_session = None

    def engine(self):
        return create_engine("sqlite:///bank.db", echo=True)

    def db_session(self):
        if not DBSession.current_db_session:
            Session = sessionmaker(bind=self.engine(), autocommit=False, autoflush=False)
            DBSession.current_db_session = Session()
        return DBSession.current_db_session

def init_db():
    db_session = DBSession()
    Base.metadata.create_all(bind=db_session.engine())