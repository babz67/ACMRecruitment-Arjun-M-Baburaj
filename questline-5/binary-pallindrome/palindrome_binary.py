def check_palindrome(num):
    """
    Enter a decimal number, and the function converts it into binary and checks if the binary string is a palindrome or not.
    Returns True if the binary string is a palindrome, False otherwise.
    """
    
    binary = bin(num)[2:]
    return binary == binary[::-1]


print("Is 5 a palindrome in binary?", check_palindrome(5))
print("Is 10 a palindrome in binary?", check_palindrome(10))
