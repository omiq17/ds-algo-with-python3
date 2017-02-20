# 1. uses linear search to find the smallest number at first
# 2. then put it at front
# 3. repeat step 1 & 2 until fully sorted

li = [int(x) for x in input("Give the numbers to be sorted "+
        "(separated by space): ").split()]
n = len(li)
for i in range(n-1):
    temp = li[i]
    index = i
    for j in range(i,n):
        #finding out the smallest number of the remaining list
        if(li[j]<temp):
            temp = li[j]
            index = j

    #swap two variables
    li[i],li[index] = li[index],li[i]

#converting list int elements to str
li = [str(x) for x in li]
print(" ".join(li))
