# CS160 Project
## Topic: Compare the difference between the regular insertion sort and insertion sort using Dynamic Programming over resursion
### Insertion Sort
- In an iterative approach
```
def it(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
```
Iterative growth of a head (“sorted” sublist) of a list A[0,i-1] compare to iterative growth of a tail (“sorted” sublist) of a list A[i,n-i]. 

n − 1 iterations (stages) i = 1, 2, . . . , n − 1;
j; 1 ≤ j ≤ i, comparisons and j or j−1 moves per stage:
1. Initialisation: the head sublist of size 1.
2. Iteration: until the tail sublist is empty, repeat:
    - Choose the first element, x = a[i] in the tail sublist.
    - Find the last element, y=a[j];1≤j≤i−1,in the head sublist not exceeding x.
    - Insert x after y in the head sublist.
3. Runtime is O(n) in best case, O(n^2) in worst and average case.
- In a recursive approach
```
def re(arr,n):
    if n>0:
        re(arr,n-1) \\ statement A
        if arr[n]>=arr[n-1]:
            return
        swap(arr,n-1,n)
        re(arr,n-1) \\ statement B
```
First recursively sort the sublist of array which is of size n-1.
Insert the last element of array into the sorted sublist.

The Time Complexity of the algorithm is still O(n^2) in the worst case. Moreover, these versions are potentially slower since repeated swapping requires more operations. However, this version is discussed because its implementation shows that statement A and B leads to a very high overlapping, which inspires us to apply dynamic programming.

### Insersion Sort using Dynamic Programming technique
Coding Insertion Sort in the recursive approach allows us realize that the statement A and statement B are subproblems overlapping of high degree. In order not to calculate the same subproblems several times, we use dynamic programming to store the solutions of those subproblems and then use them directly later. Here's the presudocode of insertion sort using dynamic programming.
```
def dp(arr,n):
    if n>0:
        if arr[n].visited != 1: 
        // if the element in the n position has not been sorted
            dp(arr,n-1) \\ statement A
            if arr[n]>=arr[n-1]:
                arr[n].visited = 1
                // Mark that we have already sorted element in this position
                return
        swap(arr,n-1,n)
        arr[n-1].visited = 1
        // Mark that we have not sort element in (n-1) position.
        dp(arr,n-1) \\ statement B
        arr[n].visited =1
```
As we use botttom up dynamic programming, we can achieve insertion sort faster, since we use memorization to store the solution of the statement B.

**What is the difference between dynamic programming and resursion?**

During the recursion, there might exist cases that same subproblems are calculated multiple times. However, Dynamic Programming is a technique which uses a table to store all the subproblems. Therefore, if we encounter the same subproblems, we do not need to calculate it again. Instead, we could directly have the results for subproblems.

We could say that recursion plays important role when we need to break problems into small subproblems. Since some subproblems are called several times during calculation, we use dynamic programming technique to store the solutions of those subproblems so that we do not need to recalculate them.

While this means that dynamic programming is not useful when there's no solutions of subproblems needed again and again. For example, the binary search does not have common subproblems.

### How to Use:
Run
'''python3 IS_iteration.py'''
'''python3 IS_recursion.py'''
'''python3 IS_DP.py'''

### Reference
Deepak Abhyankar, Maya Ingle / International Journal of Engineering Research and Applications
(IJERA)
ISSN: 2248-9622 www.ijera.com