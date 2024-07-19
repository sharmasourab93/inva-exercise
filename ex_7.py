# Create a module with about code where input will be numbers to be
# generated and output will be array of fibonacci numbers


def generate_fib_series(num):

    if num <= 0:
        return []

    fib_seq = [0, 1]
    for i in range(2, num):
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)

    return fib_seq


if __name__ == '__main__':

    num = 20
    fibonacci_numbers = {num: generate_fib_series(num)}
    print(fibonacci_numbers)
