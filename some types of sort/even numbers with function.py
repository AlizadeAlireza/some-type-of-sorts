def even(a):
#define the numbers that their result is equal to zero(0)
    return a%2 == 0
numbers = [3, 4, 2, 1, 5, 6, 9, 8, 10]

evens = filter(even, numbers)
print(sorted(list(evens)))