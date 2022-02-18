def fib(n):
    i = 0
    F1 = 1
    F2 = 1

    while i < n - 2:
        FS = F1 + F2
        F1 = F2
        F2 = FS
        i += 1
    return(F2)

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
