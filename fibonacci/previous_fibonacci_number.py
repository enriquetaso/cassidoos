# June 19 2022
# Given a Fibonacci number, give the previous Fibonacci number.
# If the number given is not a Fibonacci number, return -1. 

# Solution using Closures
# https://realpython.com/inner-functions-what-are-they-good-for/#retaining-state-with-inner-functions-closures

# Example
# In [1]: from previous_fibonacci import previous_fibonacci

# In [2]: sample_fibonacci = previous_fibonacci()

# In [3]: sample_fibonacci(34)
# Out[3]: 21

# In [4]: sample_fibonacci(35)
# Out[4]: -1

def previous_fibonacci():
    fibonacci = [0, 1]
    def inner_mean(n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
              
        if n in fibonacci:
            index = fibonacci.index(n)
            return fibonacci[index-1]
        
        while n not in fibonacci:
            fib_number = fibonacci[-2] + fibonacci[-1]
            fibonacci.append(fib_number)
            if n == fib_number:
                return fibonacci[-2]
            if n < fib_number:
                return -1
    return inner_mean
