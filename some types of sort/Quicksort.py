def quick_sort(alist, start, end):
#sort the list from index start to end - 1
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and alist[i] <= pivot):
            i += 1
        while (i <= j and alist[j] >= pivot):
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
alist = input("enter the list of numbers: ").split()
alist = [int (x) for x in alist]
quick_sort(alist, 0, len(alist))
print("sorted list: ", end = '')
print(alist)