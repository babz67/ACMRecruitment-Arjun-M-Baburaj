def encrypt(words, key):
    import string
    letters = string.ascii_letters[26:]
    
    encrypted_str = ""
    
    for i in range(len(words)):
        if words[i] in letters:
            new_index = letters.index(words[i]) + key + 1
        if new_index > 26:
            new_index -= 26
        encrypted_str += letters[new_index - 1]

    return encrypted_str



def decrypt(words, key):
    import string
    letters = string.ascii_letters[26:]
    
    decrypted_str = ""
    
    for i in range(len(words)):
        if words[i] in letters:
            new_index = letters.index(words[i]) - key + 1
        if new_index > 26:
            new_index -= 26
        decrypted_str += letters[new_index - 1]
        
    return decrypted_str


print("------Caesar Cipher Encryption and Decryption------\n")

print("The string is RECRUIT")
shifted_string = encrypt("RECRUIT", 3)
print("The string after encryption is:", shifted_string)
print("The string after decryption is:", decrypt(shifted_string, 3))

print("\nThe string is ZHOFRPH")
shifted_string = encrypt("ZHOFRPH", -3)
print("The string after encryption is:", shifted_string)
print("The string after decryption is:", decrypt(shifted_string, -3))