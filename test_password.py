import hashlib

def test_password(test, correct):
    aux = hashlib.sha256(test.encode('utf-8')).hexdigest()

    return test==correct

with open ('correct.txt','r') as password_f:
    test = password_f.read()
    test = hashlib.sha256(test.encode('utf-8')).hexdigest()

with open ('hash.txt', 'r') as hash_f:
    hash = hash_f.read()

if (test_password(test, hash)):
    print('A senha está correta!')
else:
    print('A senha está incorreta!')