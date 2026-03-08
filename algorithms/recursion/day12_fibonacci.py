"""Fibonacci sequence is the sum of the two numbers before it.
Mathematically:
F(n)=F(n-1)+F(n-2)"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci (n-2)

def printfib(n):
    for i in range(n):
        print(fibonacci(i))

def shortcutprint(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        a, b = b , a + b
    
    """ new_a = old_b
        new_b = old_a + old_b"""

n = 5

printfib(n)
shortcutprint(n)