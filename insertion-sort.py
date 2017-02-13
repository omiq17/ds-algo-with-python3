li = [int(x) for x in input("Give the numbers to be sorted (separated by space): ").split()]
n = len(li)

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if(li[j]>=li[i]):   #checking the left list item is greater or not
            li[i],li[j] = li[j],li[i] #swap two variables
            i = i-1

li = [str(x) for x in li] #converting list int elements to str
print(" ".join(li))
