
def check_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        return True
    return False


def pt_prime(st,end):
    for i in range(st, end+1):
        if check_prime(i):
            print(i, end=" ")


st_rng = int(input("Enter the starting range :- "))
end_rng = int(input("Enter the ending range :- "))
print("All the prime numbers from ", st_rng, " to ", end_rng, " :- ",end=" ")
pt_prime(st_rng, end_rng)