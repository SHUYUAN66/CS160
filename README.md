# CS160 Project
## Topic:Compare the difference between the regular insertion sort and insertion sort using Dynamic Programming over resursion
### Insertion Sort
In an iterative approach
In a recursive approach

### Insersion Sort using Dynamic Programming technique
What is the difference between dynamic programming and resursion?
During the recursion, there might exist cases that same subproblems are calculated multiple times. However, Dynamic Programming is a technique which uses a table to store all the subproblems. Therefore, if we encounter the same subproblems, we do not need to calculate it again. Instead, we could directly have the results for subproblems.

We could say that recursion plays important role when we need to break problems into small subproblems. Since some subproblems are called several times during calculation, we use dynamic programming technique to store the solutions of those subproblems so that we do not need to recalculate them.

While this means that dynamic programming is not useful when there's no solutions of subproblems needed again and again. For example, the binary search does not have common subproblems.
