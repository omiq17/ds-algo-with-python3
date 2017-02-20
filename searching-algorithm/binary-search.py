# 1. at first sort the list
# 2. run a while loop
# 3. divide the list
# 4. compare the middle elemment of list with the searching element
# 5. if mathches, then return true
# 6. otherwise, slice the list
# 7. when only one element in the list remains check directly with
#    searching element. If mathches then true, otherwise false

li = [int(x) for x in input("Give the numbers to be sorted "+
        "(separated by space): ").split()]
find = 15
li.sort()

while True:
    n = len(li)
    #when it comes to last element check here
    if(n==1 and li[0]==find):
        result = True
    else:
        result = False

    #divide the list
    div = int(n/2)

    #comparing with find elemment
    if(li[div] == find):
        result = True
        break
    elif(li[div]<find):
        #slicing the list [startIndex:endIndex]
        li = li[div+1:n]
    else:
        li = li[0:div-1]

print(result)
