def caching_fibonacci():
    """
    Creates a dictionary for the cache, where we will store already calculated values.
    """
    cashe = {}

    def fibonnachi(n):
        # Basic conditions for recursion
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Check if the result is in the cache
        elif n in cashe:
            return cashe[n]
        
        # Calculate the Fibonacci number if it is not already cached
        cashe[n] = fibonnachi(n - 1) + fibonnachi(n - 2)
        return cashe[n]
    
    return fibonnachi

fib = caching_fibonacci()

# Test case
print(fib(10))
print(fib(15))