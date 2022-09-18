
def check_co_prime(n1,n2):
    small = n1
    if n1 > n2:
        small = n2
    hcf = 0
    for i in range(1, small+1):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    if hcf == 1:
        return True
    return False


print("Enter two numbers:- ")
n1 = int(input())
n2 = int(input())
if check_co_prime(n1, n2):
    print(n1," ",n2,"are co-prime number")
else:
    print(n1," ",n2,"are not co-prime number")