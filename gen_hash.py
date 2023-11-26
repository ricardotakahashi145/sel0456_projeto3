import hashlib

correct_password = 'ricardo123'
wrong_password = 'ricardo321'
hash_password = hashlib.sha256(correct_password.encode('utf-8')).hexdigest()

with open('hash.txt', 'w') as f:
    f.write(hash_password)

with open('correct.txt', 'w') as f:
    f.write(correct_password)

with open('wrong.txt', 'w') as f:
    f.write(wrong_password)