def caching_fibonacci():
    cashe = {}

    def fibonnachi(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cashe:
            return cashe[n]
        
        cashe[n] = fibonnachi(n - 1) + fibonnachi(n - 2)
        return cashe[n]
    
    return fibonnachi

fib = caching_fibonacci()
print(fib(10))
print(fib(15))