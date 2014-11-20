__author__ = 'timyu'
#demonstrate the usage of generator
def fib(max):
    n, a, b = 0, 0 , 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

list = fib(5)
for l in list:
    print l