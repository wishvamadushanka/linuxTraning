import sys
import hashlib
import os

salt = os.urandom(32)
dk = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode(), salt, 200000)
print(dk.encode('hex_codec'))
#print(binascii.hexlify(dk).decode())
#print(binascii.hexlify(dk).decode('ascii'))
#print(type(salt))
#salt=unicode(salt, 'utf-8')
#print(salt.decode('hex_codec'))
