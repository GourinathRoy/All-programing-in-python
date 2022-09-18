
def is_even(n):
    if n % 2 == 0:
        return True
    return False


def pt_even_number(n):
    while n > 0:
        if is_even(n):
            print(n, end=" ")
        n = n - 1


n = int(input("Enter your range:- "))
pt_even_number(n)
