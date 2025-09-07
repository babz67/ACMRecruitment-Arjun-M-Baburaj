import base64

def decrypt_caesar(words, key):
    import string
    letters = string.ascii_letters[26:]
    words = words.upper()
    decrypted_str = ""
    
    for i in range(len(words)):
        if words[i] in letters:
            new_index = letters.index(words[i]) - key + 1
        if new_index > 26:
            new_index -= 26
        decrypted_str += letters[new_index - 1]
        
    return decrypted_str


message = "55485a6a64584a6c55474a6c63673d3d"
print("The encrypted message is:", message)

decoded_bytes = bytes.fromhex(message)
message = decoded_bytes.decode("utf-8")

decoded_bytes = base64.b64decode(message)
message = decoded_bytes.decode("utf-8")

message = decrypt_caesar(message, 13)

print("The decrypted message is:", message)