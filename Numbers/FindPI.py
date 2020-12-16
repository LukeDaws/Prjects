#This is to find the nth digit of pi
#Pi is calculated using the Chudnovsky algorithm
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm

import decimal

def Find_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    L = 13591409
    X = 1
    M = 1
    K = 6
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C/S
    return pi

def main():

    n = int(input("Please enter the number of decimals to calculate pi to: "))
    print(Find_pi(n))

if __name__ == '__main__':
    main()
