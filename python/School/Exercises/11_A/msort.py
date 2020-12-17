def mergesort(arr, f): 
    if len(arr) > 1: 
        # Sort halves into separate memory
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L, f)
        mergesort(R, f)

        # Merge L and R back into arr 
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if f(L[i], R[j]): 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Finish the merge by copying any leftover elements 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def by_id(x, y):
    return x[0] < y[0]

def by_name(x, y):
    x_name = x[1].split(' ')
    y_name = y[1].split(' ')
    if x_name[-1] == y_name[-1]:
        return x_name[0] < y_name[0]
    else:
        return x_name[-1] < y_name[-1]

if __name__ == "__main__":
    alist = [4,3,7,1,9]
    b_list = [('124543', 'Jack Adams'), ('845567', 'Susie Marigold'), ('656234', 'Douglas Adams')]
    mergesort(alist,lambda x,y: x > y)
    test_tuple = ()
    print("Alfred Bigglesworth".split())
    # print(alist)        # [9, 7, 4, 3, 1]
