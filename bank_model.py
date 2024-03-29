from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(60), nullable=True)
    lastname = Column(String(60), nullable=False)
    email = Column(String(120), nullable=True)
    accounts = relationship('Account', back_populates='customer')
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), index=True, nullable=False)
    bank = relationship('Bank', back_populates='customers')


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
    fk_customer_id = Column(Integer, ForeignKey(Customer.id), index=True, nullable=False)
    customer = relationship(Customer, back_populates='accounts')
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), index=True, nullable=False)
    bank = relationship('Bank', back_populates='accounts')

    def __init__(self, customer):
        self.customer = customer

    def deposit(self, amount):
        #TODO add throwing exception when amount is invalid
        if not self.balance:
            self.balance = 0
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
    customers = relationship(Customer, back_populates='bank')
    accounts = relationship(Account, back_populates='bank')

    def __init__(self, name):
        self.name = name

    def create_customer(self, firstname, lastname, email):
        c = Customer(firstname, lastname, email)
        c.bank = self
        return c

    def create_account(self, customer):
        a = Account(customer)
        a.bank = self
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
        return f'Bank:\n{self.name}\n{self.customers}\n{self.accounts}\n----------'


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