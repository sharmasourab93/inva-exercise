from functools import cache


# Create fibonacci series with recursive function for 10 numbers
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
#


@cache
def fib_n(n):
    if n == 0 or n==1:
        return n

    return fib_n(n-1) + fib_n(n-2)


def generate_fib_n(nos: int = 10):
    for i in range(nos):
        print(fib_n(i))


if __name__ == '__main__':
    generate_fib_n()
