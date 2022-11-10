email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach#sgh.waw.pl'
email3 = '@sgh.waw.pl'
email4 = 'pawel@'
email5 = 'pawel@.pl'
email6 = 'pa@wel@wwa.pl'
email7 = 'ab@sgh@waw@pl'
email8 = 'pawel@pl.'
email9 = 'pawel@gmail.com'


def check_email(email):
    if not email:
        return False
    # TODO implement different checks
    if not (email.find('@') > 0 and email.find('@') < len(email)-1):
        print('@ not found or in wrong position')
        return False
    if not (email.find('@') == email.rfind('@')):
        print('@ too many of them')
        return False
    #TODO check for @. in email
    return True


for em in [email1, email2, email3, email4, email5, email6, email7, email8, email9]:
    print('{}: {}'.format(em, check_email(em)))

#for i in range(len(email4)):
#    print(email4[i])