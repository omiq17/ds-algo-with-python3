### This code is applicable only for positive values

# importing math library for power operation
import math

# li = [int(x) for x in input("Give only the positive numbers to be sorted "+
#         "(separated by space): ").split()]
li = [ 130, 4,3,5,57,333, 2943, 9, 47, 345, 3454 ,5, 49]
m = max(li)
n = len(str(m))

for i in range(n):
    #initializing a 2D list
    temp_li = [[] for y in range(10)]
    for j in range(len(li)):
        #first dividing the number accordingly 1,10,100...
        #and then take modulus of 10
        #at last append the number to newly created 2D list according to their..
        #radix digit
        temp = int(li[j]/math.pow(10, i))
        digit = int(temp%10)
        temp_li[digit].append(li[j])

    #making the input list empty for re-arranging
    li = []
    #looping through the 2D list and add numbers to list according to order
    for i in range(len(temp_li)):
        for j in range(len(temp_li[i])):
            li.append(temp_li[i][j])

print(li)
