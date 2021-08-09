import sys
import hashlib
import os

salt = os.urandom(32)
dk = hashlib.sha512(salt + sys.argv[1].encode()).hexdigest()
print(dk)
