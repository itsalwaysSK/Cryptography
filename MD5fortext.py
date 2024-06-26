#Wap to create MD5 hash for bob and alice

import hashlib

md5hasher = hashlib.md5(b'alice')
alice_hash = md5hasher.hexdigest()
print("Hash of text, alice is: \n", alice_hash)

md5hasher = hashlib.md5(b'bob')
bob_hash = md5hasher.hexdigest()
print("Hash of text, bob is: \n", bob_hash)
