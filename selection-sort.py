li = [int(x) for x in input("Give the numbers to be sorted (separated by space): ").split()]
n = len(li)
for i in range(n-1):
    temp = li[i]
    index = i
    for j in range(i,n):
        if(li[j]<temp):   #finding out the smallest number of the remaining list
            temp = li[j]
            index = j

    li[i],li[index] = li[index],li[i] #swap two variables
