import sys

def xor(plaintext, key):
    result = bytearray()
    key = bytearray(key, encoding='UTF-8')
  
    # XOR every byte of the plaintext with the corresponding byte from the key  
    for i in range( len(plaintext) ):
        k = key[i % len(key)]
        c = plaintext[i] ^ k
        result.append(c)
      
    return result

# Read file as byte array
ciphertext = bytearray(open(sys.argv[1], 'rb').read())
# convert
plaintext = xor(ciphertext, sys.argv[3])
# Open outputfile and write result
with open(sys.argv[2], "wb") as output:
    output.write(plaintext)
