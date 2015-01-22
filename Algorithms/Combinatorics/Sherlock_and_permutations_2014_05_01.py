#solution toward https://www.hackerrank.com/challenges/sherlock-and-permutations
#written in Python on 2015-01-22
import math
def main():
    n = int(raw_input())
    for _ in range(n):
        n,m = [int(x) for x in raw_input().strip().split()]
        print math.factorial(n + m - 1) / math.factorial(m - 1) /  math.factorial(n) % (10 ** 9 + 7)

if __name__ == '__main__':
    main()