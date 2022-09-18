
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    return False



def generate_prime_number(n):
    count = 0
    num = 2
    while count != n:
        if is_prime(num):
            print(num, end=" ")
            count = count + 1
        num = num + 1


n = int(input("Enter how many numbers you want to print:- "))
print("First ", n, "prime numbers are :- ", end=" ")
generate_prime_number(n)
