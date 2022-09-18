
def check_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0 :
            count = count + 1
    if count == 2:
        return True
    return False


def find_next_prime(n):
    next_num = n
    while ( True ):
        for i in range(n, next_num+1):
            if check_prime(i):
                return i
            next_num = next_num + 1


n = int(input("Enter a number :- "))
print("The next prime number of ", n, "is :- ", find_next_prime(n+1))
