
import math

n = int(input("enter an integer number to check "))

if n <= 1:
    print("not prime")
elif n <= 3:
    print("prime")  # 2&3 are primery num
elif n % 2 == 0 or n % 3 == 0:
    print("not prime")
else:
    is_prime = True
    c = 5
    while c * c <= n:
        if n % c == 0 or n % (d + 2) == 0:
            is_prime = False
            break
        d += 6
    print("prime" if is_prime else "not prime")
