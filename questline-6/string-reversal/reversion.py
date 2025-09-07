def rec_revstr(s):
    if len(s) <= 1: # No need to reverse if string is empty or has one character
        return s
    else: # returns the last character and calls itself on the remaining string
        return s[-1] + rec_revstr(s[:-1])

print("---Reversing string using recursion---")
print("String before recursion: Hello")
print("String after recursion:", rec_revstr("Hello"))


print("\n---Reversing string using iteration---")
def iter_revstr(s):
    result = "" # an empty string to store the reversed string
    for char in s: # Loops through each character in string
        result = char + result # adds individual characters at the start of the string
    return result

print("String before iteration: Hello")
print("String after iteration:", iter_revstr("Hello")) 
