email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach#sgh.waw.pl'
email3 = '@sgh.waw.pl'
email4 = 'pawel@'
email5 = 'pawel@.pl'


def check_email(email):
    #TODO implement different checks
    if email:
        return True
    else:
        return False


for em in [email1, email2, email3, email4, email5]:
    print('{}: {}'.format(em, check_email(em)))