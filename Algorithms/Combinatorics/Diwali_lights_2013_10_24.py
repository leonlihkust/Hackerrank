#solution toward https://www.hackerrank.com/challenges/diwali-lights
#written in Python on 2015-01-22
def main():
    n = int(raw_input())
    for _ in range(n):
        bulbs = int(raw_input())
        print (2 ** bulbs - 1) % (10 ** 5)
if __name__ == '__main__':
    main()