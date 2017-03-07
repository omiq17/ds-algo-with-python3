### This code can compute within any range of values
### This code is also valid for negative values

#for addusting the range according to list's first index 0
def findAdjust():
    adjust = 0

    if m>0:
        adjust = 0-m
    elif m<0:
        adjust = m - (2*m)

    return adjust

#make the count list
def makeCount(n,range_li):
    count = [0] * range_li

#increase value in count list for each occurance of a value in
#input list. Here count list's index denotes input list's value
    for i in range(n):
        temp = li[i] + adjust
        count[temp] = count[temp] + 1

#increasing values of the list according to previous value
    for i in range(range_li-1):
        count[i+1] = count[i] + count[i+1]

    return count

#make sorted list
#by comparing & calculating input list and count list
def countSort(n,count,adjust):
    sorted_list = [0] * n

#input list's value denotes count list's index
#count list's value denotes output(sorted_list) list's index and..
#then decrease the value by one
#put input list's value to output list's index
#like that we connect three lists here to generate output list
    for i in range(n):
        input_value = li[i]
        count_index = input_value + adjust
        count_value = count[count_index]
        count[count_index] = count_value - 1
        sorted_list[count_value-1] = input_value

#always return list that is created in a function
#otherwise it will be disappeared when function destroys
    return sorted_list



li = [int(x) for x in input("Give the numbers to be sorted "+
        "(separated by space): ").split()]
# li = [ 1, 3,3,5,7,-3, -2, -9, -7, 5, 4 ,5, 9]
n = len(li)
m = min(li)
range_li = max(li) - m + 1

adjust = findAdjust()
count = makeCount(n,range_li)
sorted_list = countSort(n,count,adjust)

#converting list int elements to str
sorted_list = [str(x) for x in sorted_list]
print("The sorted list is: ")
print(" ".join(sorted_list))
