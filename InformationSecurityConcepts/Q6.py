import sys
import hashlib

dk = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode(), b'Km5d5ivMy8iexuHcZrsD', 200000)
print(dk.encode('hex_codec'))
#print(binascii.hexlify(dk).decode())
#print(binascii.hexlify(dk).decode('ascii'))
