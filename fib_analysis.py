import cProfile
import pstats

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n-1):
        temp = b
        b = a + b
        a = temp
    return b

def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

assert fibo(12) == fibonacci(12)

if __name__ == "__main__":
    cProfile.run('fibo(28)', 'filename.txt')
    p = pstats.Stats('filename.txt')
    p.strip_dirs().print_stats()

    
    cProfile.run('fibonacci(28)', 'filename.txt')
    p = pstats.Stats('filename.txt')
    p.strip_dirs().print_stats()
