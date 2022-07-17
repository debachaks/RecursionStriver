def f_recursive(i,arr,n):
    if i>=n/2:
        return
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1]=temp
    f_recursive(i+1,arr,n)
    
arr = [1,2,3,4,5,6]
f_recursive(0,arr,6)
print(arr)
