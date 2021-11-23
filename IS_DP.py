def swap(arr,p1,p2):
    temp=arr[p1]
    arr[p1]=arr[p2]
    arr[p2]=temp
    
def re(arr,n):
    code = [0]*(n+1)
    if n>0:
        if code[n] ==1:
            re(arr,n-1)
            if arr[n]>=arr[n-1]:
                code[n] =1
            return
        swap(arr,n-1,n)
        code[n-1] =0
        re(arr,n-1)
        code[n] =1
            
            
arr = [12, 11, 13, 5, 6]
n = len(arr)-1
re(arr, n)
for i in range(len(arr)):
    print("% d" % arr[i])
