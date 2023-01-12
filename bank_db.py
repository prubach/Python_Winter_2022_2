from bank_model import init_db, Bank, DBSession

db = DBSession().db_session()

def initialize():
    init_db()
    bank = Bank('Python Bank')
    db.add(bank)
    db.commit()


def add_data():
    b = db.query(Bank).filter(Bank.id==1).first()
    print(b)

    c1 = b.create_customer('John', 'Smithson', None)
    db.add(c1)
    a1 = b.create_account(c1)
    db.add(a1)
    a1.deposit(1000)
    db.merge(a1)

    c2 = b.create_customer('Anne', 'Brown', 'anne@brown')
    a2 = b.create_account(c2)
    db.add(a2)
    a2.deposit(2000)
    db.add(a2)

    # #a = Account(c1)
    # print(a1)
    # a1.deposit(100)
    # print(a1)
    # a1.charge(50)
    # print(a1)
    # a2 = b.create_account(c1)
    # print('Before transfer')
    # print(b)
    db.commit()


if __name__ == '__main__':
    #initialize()
    add_data()



#
# #c1 = Customer('John', "Smith")
# b = Bank()
# c1 = b.create_customer('John', 'Smith')
# print(c1)
# print(b)
# a1 = b.create_account(c1)
# #a = Account(c1)
# print(a1)
# a1.deposit(100)
# print(a1)
# a1.charge(50)
# print(a1)
# a2 = b.create_account(c1)
# print('Before transfer')
# print(b)
#
# a_from = b.find_account(1001)
# print('account from')
# print(a_from)
#
# b.transfer(1001, 1002, 20)
# print('After transfer')
# print(b)
#
