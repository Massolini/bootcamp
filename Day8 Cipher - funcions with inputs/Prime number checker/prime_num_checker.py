def prime_checker(number):
    n=number
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    #return a
    print(n)
    print(a)
    if n == a[0]:
        print(f"The number {a} is a Prime number")
    elif n != a[0]:
        print(f"The number {n} is a Composit number")
    
# def trial_division(n: int): #-> List[int]:
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1: a.append(n)
#     # Only odd number is possible
#     #return a
#     print(a)

n = int(input("Check this number: "))
prime_checker(number=n)
#trial_division(n)