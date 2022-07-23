def linearSearch(A, x):
#search the element x at A,
#if find then return the index, otherwise return -1(incorrect value or not finding)
    n = len(A)
    for i in range(0, n):
        if(A[i] == x):
            return i
        
    return -1
        
def main():
    h = []
    f = int(input("ur number for ur sort linear list: "))
    while f > 0 :
        int(input("num for ur list: ")).append(h)
        
    print(linearSearch(A, int(input("ur num:  "))))
if __name__ == "__main__":
    main()