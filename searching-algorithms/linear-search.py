li = [int(x) for x in input("Give numbers for searching "+
        "(separated by space): ").split()]
# li = [ 130, 4,33,5,57,333, 2943, 9, 47, 345, 3454 ,5, 49]
search = [int(x) for x in input("Give the number to search "+
        "(separated by space): ").split()]
# search = 333

# flag varible
found = False
for i in range(len(li)):
    # check list items one by one
    if search == li[i]:
        print("Searching element is found.")
        found = True

if found == False:
    print("Searching Element is not found.")
