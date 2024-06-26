#wap to create SHA-1 and SHA-256 hash

import hashlib

print("SHA-1 has of word alice is:\n", hashlib.sha1(b'alice').hexdigest())
print("SHA-256 has a word alice is:\n", hashlib.sha256(b'alice').hexdigest())