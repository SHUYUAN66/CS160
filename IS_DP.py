def swap(arr,p1,p2):
    temp=arr[p1]
    arr[p1]=arr[p2]
    arr[p2]=temp
    
def re(arr,n):
    if n>0: 
        if list(arr[n].values())[0]!=1:
            re(arr,n-1)
            if list(arr[n].keys())[0]>=list(arr[n-1].keys())[0]:
                list(arr[n].values())[0] =1
                return
            swap(arr,n-1,n)
            arr[n-1].update({list(arr[n-1].keys())[0]:0})
            re(arr,n-1)
            arr[n].update({list(arr[n].keys())[0]: 1})
            
            
arr = [{12: 0}, {11: 0}, {13: 0}, {5: 0}, {6: 0}]
n = len(arr)-1
re(arr, n)
for i in range(len(arr)):
    print(list(arr[i].keys())[0])
