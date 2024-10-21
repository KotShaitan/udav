def different_digits_number_search(arr):
    for i in range(len(arr)):
        c=0
        for j in str(arr[i]):
            for n in str(arr[i]):
                if j == n:
                    c += 1
        if c == len(arr[i]):
            return arr[i]
            
    return -1

        
arr = [22, 111, 101, 124, 33, 30]
print(different_digits_number_search(arr))