import sys

def repeating_key_xor(plaintext, key):
    if len(key) == 0 or len(key) > len(plaintext):
        raise "KEY LENGTH EXCEPTION!"
  
    ciphertext_bytes = bytearray()
    key_bytes = bytearray(key, encoding='UTF-8')
  
    # XOR every byte of the plaintext with the corresponding byte from the key  
    for i in range( len(plaintext) ):
        k = key_bytes[i % len(key)]
        c = plaintext[i] ^ k
        ciphertext_bytes.append(c)
      
    return ciphertext_bytes

# Read file as byte array
plaintext = bytearray(open(sys.argv[1], 'rb').read())

with open(sys.argv[2], "wb") as output:
    result = repeating_key_xor(plaintext, sys.argv[3])
    output.write(result)
