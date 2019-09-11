# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    a, b = 1, 1

    for i in range(n - 1):
        a, b = b, a + b
    return a
