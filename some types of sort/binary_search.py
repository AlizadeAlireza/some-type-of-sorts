def binary_search(alist, key):
#Find key in alist[start...end - 1]
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end) // 2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1
    
alist = input("enter the sorted list of numbers: ")# like 2 , 3 , 5 , 6
alist = alist.split()
alist = [int (x) for x in alist]
key = int(input("the number to search for : "))
index = binary_search(alist, key)
if index < 0:
    print("{} was not found.". format(key))
else:
    print("{} was found at index {}.". format(key, index))
