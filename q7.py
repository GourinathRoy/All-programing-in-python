

def find_fact(n):
    if n == 0:
        return 1
    return n * find_fact(n-1)



def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    return False


n = int(input("Enter a number to find the factorial:- "))
if is_prime(n):
    print("Factorial of ",n," is :- ", find_fact(n))
else:
    print("Number is not prime , enter a prime number")
