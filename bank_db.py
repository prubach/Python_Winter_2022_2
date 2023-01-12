from bank_model import init_db, Bank, DBSession

db = DBSession().db_session()

def initialize():
    init_db()
    bank = Bank('Python Bank')
    db.add(bank)
    db.commit()

if __name__ == '__main__':
    initialize()



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
