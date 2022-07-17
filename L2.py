#Print names n times , TC:O(N),SC:O(N)
def f(i,n):
    #base case
    if i > n:
        return
    print("Debaleena")
    f(i+1,n)

n = int(input("Enter a number "))   
f(1,n)


#Print 1 to n
def f2(i,n):
    #base case
    if i > n:
        return
    print(i)
    f2(i+1,n)

n = int(input("Enter a number: "))
f2(1,n)

#print from 1 to n using backtracking
def f2_back(i,n):
    if i<1:
        return
    f2_back(i-1,n)
    print(i)
    
n = int(input("Enter a number: "))
f2_back(n,n)

#print from n to 1
def f3(n):
    if n<1:
        return
    print(n)
    f3(n-1)

n = int(input("Enter a number: "))
f3(n)  

#print from n to 1 using backtracking
def f3_back(i,n):
    if i > n:
        return
    f3_back(i+1,n)
    print(i)
    
n = int(input("Enter a number: "))
f3_back(1,n) 
