
def check_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    return False


a = int(input("Enter a number for check it is prime or not :- "))
if check_prime(a):
    print(a , "is prime number")
else:
    print(a ,"is not a prime number")
