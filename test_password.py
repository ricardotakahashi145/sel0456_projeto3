import hashlib

def test_password(test, correct):
    aux = hashlib.sha256(test.encode('utf-8')).hexdigest()

    return test==correct

with open ('correct.txt','r') as password_f:
    test = password_f.read()
    test_hash = hashlib.sha256(test.encode('utf-8')).hexdigest()

with open ('hash.txt', 'r') as hash_f:
    hash = hash_f.read()

with open('correct.txt', 'r') as correct_f:
    correct = correct_f.read()

print('A senha lida é:', test)
print('A senha correta é:', correct)

if (test_password(test_hash, hash)):
    print('A senha está correta!')
else:
    print('A senha está incorreta!')