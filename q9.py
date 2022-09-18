
def find_hcf(n1, n2):
    small = n1
    if n1 > n2:
        small = n2
    hcf = 0
    for i in range(1, small+1):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    return hcf


print("Enter two numbers:- ")
n1 = int(input())
n2 = int(input())
print("hcf of ",n1," ",n2,"is :- ", find_hcf(n1, n2))