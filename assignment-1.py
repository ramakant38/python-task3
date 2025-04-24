def factorial(n):
    if n <= 2:
        return n
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
res = factorial(n)

print("The factorial of ",n," is ",res)