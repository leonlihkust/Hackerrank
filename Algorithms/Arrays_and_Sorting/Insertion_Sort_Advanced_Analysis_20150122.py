#solution toward https://www.hackerrank.com/challenges/insertion-sort
#written in Python on 2015-01-12
def merge_sort(ar):
    if len(ar) == 1:
        return 0,ar
    mid = len(ar) / 2
    left_inversions, left = merge_sort(ar[:mid])
    right_inversions, right = merge_sort(ar[mid:])
    merge_inversions, sortList = merge(left,right)
    inversions = left_inversions + right_inversions + merge_inversions
    return inversions, sortList

def merge(left,right):
    sortList = []
    i = 0
    j = 0
    shiftCount = 0
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            sortList.append(left[i])
            i += 1
        elif left[i] > right[j]:
            sortList.append(right[j])
            j += 1
            shiftCount += len(left) - i
    sortList += left[i:]
    sortList += right[j:]
    return shiftCount,sortList
  
n = input()
for iterate in range( n ):
    x = input()
    a = [ int( i ) for i in raw_input().strip().split() ]
    shiftCount = 0
    shiftCount,ar = merge_sort(a)
    print shiftCount