# 1. using a for loop an element is taken from a list
# 2. checked it with the left elements with another for loop
# 3. if the left element is bigger then swap elements, otherwise break

li = [int(x) for x in input("Give the numbers to be sorted "+
        "(separated by space): ").split()]
n = len(li)

for i in range(1,n):
    for j in range(i-1,-1,-1):
        #checking the left list item is greater or not
        if(li[j]>=li[i]):
            #swap two variables
            li[i],li[j] = li[j],li[i]
            i = i-1

#converting list int elements to str
li = [str(x) for x in li]
print(" ".join(li))
