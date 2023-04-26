# PRJCTR Homework 19: Data structures and algorithms

This work shows the benefits of using self-balancing BST data structure. 
A python class was implemented with insert, search and delete operations, 
and other helpful methods for this BST. 
The complexity of this data structure was measured and worst case scenarios 
were also considered.

Integer counting sort was considered as sorting algorithm. 
The complexity of it was measured and worst case scenarios were also considered.

## Prerequisites

* Installed [python](https://www.python.org/downloads/)
* Installed required libs: `pip install -r requirements.txt`

## BST

Standard implementation of the BST with self-balancing using left/right 
rotations from [AVL trees](https://en.wikipedia.org/wiki/AVL_tree).

Usage:

```python
from bst import BST

tree = BST()

for i in range(10): tree.insert(i)

tree.height()  # >>> 4
tree.balance()  # >>> -1
tree.pretty_print()
# │           ┌── 9
# │       ┌── 8
# │   ┌── 7
# │   │   │   ┌── 6
# │   │   └── 5
# │   │       └── 4
# └── 3
#     │   ┌── 2
#     └── 1
#         └── 0

tree.search(6)  # >>> True
tree.search(16)  # >>> False

tree.delete(9)
tree.delete(8)
tree.delete(7)
tree.insert(17)
tree.insert(18)
tree.insert(19)

tree.pretty_print()
# │           ┌── 19
# │       ┌── 18
# │   ┌── 17
# │   │   │   ┌── 6
# │   │   └── 5
# │   │       └── 4
# └── 3
#     │   ┌── 2
#     └── 1
#         └── 0
```

The average and worst-case performances are `O(log(n))` for search, insert and delete operations.
The worst-case scenarios are happen when the values for insertion or deletion were sorted before 
(in ascending or descending order, it doesn't matter). 
In that cases, we have to re-balance our tree almost each time after insertion or deletion.
So the best performance when we have shuffled values before insertion.

### Results

![BST operations results](./images/bst_results.png)

![BST operations results 2](./images/bst_results_2.png)

As we could see our operations performance is getting worse with regard to `log(n)` function. 

## Counting sort

Standard implementation form the [wiki](https://en.wikipedia.org/wiki/Counting_sort#Pseudocode) pseudo-code.

Usage:

```python
from counting_sort import counting_sort

arr = [1, 10, 5, 6, 7, 9, 11, 10, 16, 19, 20, 21, 3, 6, 9]

counting_sort(arr, len(arr), max(arr)) 
# >>> [1, 3, 5, 6, 6, 7, 9, 9, 10, 10, 11, 16, 19, 20, 21]
```

Counting sort algorithm operates by counting the number of objects that possess distinct key values, 
and applying prefix sum on those counts to determine the positions of each key value in the output sequence.
Its running time is linear in the number of items and the difference between the maximum key value and the minimum key value, 
so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number of items.

Worst-case performance: `O(n+k)` where k is the range of the non-negative key values.

So it doesn't perform when we have a very long range of keys. 
And performs best with a huge amount of keys in a short range. 

### Results

![Counting sort results](./images/counting_sort_results.png)

![Counting sort results 2](./images/counting_sort_results_2.png)

As we could see that longer ranges (k parameters are bigger and dots are darker) 
are always higher than smaller ranges (k parameters are smaller and dots are lighter).
