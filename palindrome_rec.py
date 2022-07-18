def f(i,arr):
    if i >= len(arr)/2:
        return True
    if arr[i] != arr[len(arr)-i-1]:
        return False
    return f(i+1,arr)
    
arr = 'MADSM'
print(f(0,arr))
