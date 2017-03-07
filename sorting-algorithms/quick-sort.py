# 1. in quickSort function, first I check the base condition
# 2. then I use the makePartition function where I divide the list
#    into two parts based on pivot
# 3. then I call the quickSort() recursively

#for partioning the list
def makePartition(lo,hi):
    pivot = hi
    pivot_val = li[hi]
    hi = hi-1

    # divide the list into two parts based on pivot
    while True:
        if lo >= hi:
            if li[lo] <= pivot_val:
                li[lo+1],li[pivot] = li[pivot],li[lo+1]
                return lo+1
            else:
                li[lo],li[pivot] = li[pivot],li[lo]
                return lo

        elif li[lo] > pivot_val:
            if li[hi] <= pivot_val:
                li[lo],li[hi] = li[hi],li[lo]
                lo = lo+1
                hi = hi-1
            else:
                hi = hi-1
        else:
            lo = lo+1


#quickSort function
def quickSort(lo,hi):
    #base condition
    if (lo >= hi):
        return

    partition = makePartition(lo,hi)

    quickSort(lo,partition-1)
    quickSort(partition+1,hi)

# li = [int(x) for x in input("Give the numbers to be sorted "+
#         "(separated by space): ").split()]
li = [2, 5, 1, 3,3,5,7,-33, -2, -999, 434, 4 ,24, 432]
n = len(li)

quickSort(0, n-1)

#converting list int elements to str
li = [str(x) for x in li]
print("The sorted list is: ")
print(" ".join(li))
