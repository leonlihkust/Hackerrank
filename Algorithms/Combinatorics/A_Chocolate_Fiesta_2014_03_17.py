#solution toward https://www.hackerrank.com/challenges/a-chocolate-fiesta
#written in Python on 2015-01-22
import math
def main():
    n = int(raw_input())
    ar = [int(x) for x in raw_input().strip().split()]
    value = False
    for i in ar:
        if i % 2 == 1:
            value = True
    if value:
        print (2 ** (n - 1) -1) % (10 ** 9 + 7) 
    else:
        print (2 ** n - 1) % (10 ** 9 + 7) 
    
if __name__ == '__main__':
    main()