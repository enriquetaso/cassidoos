# https://realpython.com/fibonacci-sequence-python/#using-iteration-and-a-python-function
# Example:
# >>> from fibonacci_class import Fibonacci
# >>> fibonacci_of = Fibonacci()
# >>> fibonacci_of(5)
# 5
# >>> fibonacci_of(6)
# 8
# >>> fibonacci_of(7)
# 13
# >>> [fibonacci_of(n) for n in range(15)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
        
        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)
        return self.cache[n]
