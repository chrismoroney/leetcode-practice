
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)


if __name__ == "__main__":
    num = fibo(10)
    print(num)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    