# project Euler problem 3

from sympy import factorint

prime_factor = list(factorint(600851475143).keys())[-1]

print(f"The largest prime factor of 6000851475143 is {prime_factor}")



# project euler problem 1

multiples = []

for i in range(1, 1001):
    if i % 5 == 0 or i % 3 == 0:
        multiples.append(i)

print("\nThe sum of the multiples of 3 and 5 below 1000 is", sum(multiples))
