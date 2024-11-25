import time


def collatz(n):
    if n == 1:
        return 1
    if n % 2:
        return collatz(3*n+1)
    else:
        return collatz(n/2)
    

def main():
    start = time.time()
    col = 2
    for col in range(1,11):
        collatz(col)
    end = time.time()
    duration = end - start
    print(duration)

if ( __name__ == "__main__" ):
    main()