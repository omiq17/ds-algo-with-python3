# 1. in mergeSort function, I divide the list and call mergeSort
#    recursively until one element remains and then call merge()
# 2. in merge function i take a new list.
#    then sort two parts of list by using if,else in a while loop

#merge fucntion
def merge(start, mid, end):
    newLi = []
    i = start
    j = mid+1

    while True:
        if i==mid+1 and j==end+1:
            k=0
            s=start
            #copy from newLi to li after sorting
            for i in li[start:end+1]:
                li[s] = newLi[k]
                s=s+1
                k = k+1
            break
        elif i==mid+1:
            newLi.append(li[j])
            j = j+1
        elif j==end+1:
            newLi.append(li[i])
            i = i+1
        elif li[i] >= li[j]:
            newLi.append(li[j])
            j = j+1
        else:
            newLi.append(li[i])
            i = i+1


#mergeSort function
def mergeSort(start,end):
    if (start >= end):
        return

    mid = int((start+end)/2)

    mergeSort(start,mid)
    mergeSort(mid+1,end)

    merge(start,mid,end)

li = [int(x) for x in input("Give the numbers to be sorted "+
        "(separated by space): ").split()]
# li = [2, 5, 1, 3,3,5,7,-33, -2, -999, 434, 4 ,24, 432]
n = len(li)

mergeSort(0, n-1)

#converting list int elements to str
li = [str(x) for x in li]
print("The sorted list is: ")
print(" ".join(li))
