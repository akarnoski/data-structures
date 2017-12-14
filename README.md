# Data Structures & Algorithms

**Introduction**

The following data structures and algorithms are solved using Python by [myself](https://github.com/adriennekarnoski) 
and [Cody Dibble](https://github.com/hcodydibble).

## Getting Started

**Check out the code**

[Click Here!](https://github.com/adriennekarnoski/data-structures/tree/master/src)

**Installation**

Clone the repository:

`$ git clone https://github.com/adriennekarnoski/data-structures`

Move into the **data-structures** directory:

`$ cd data-structures`

Start your virtual environment:

`$ python3 -m venv ENV`

`$ source bin/ENV/activate`

Install package

`$ (ENV) pip install -e .`


## Data Structures

In computer science, a data structure is a particular way of organizing 
and storing data in a computer so that it can be accessed and modified 
efficiently. More precisely, a data structure is a collection of data values, 
the relationships among them, and the functions or operations that can be applied 
to the data.[[1]](https://en.wikipedia.org/wiki/Data_structure)

***

### Linked List
Linear data structure where each element is a separate object.
 Each element of a list is comprising of two items – the data and a reference to the next node.
 [[2]](http://www.geeksforgeeks.org/overview-of-data-structures-set-1-linear-data-structures/)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.push()` | O(1) |
|`.pop()` | O(1) |
|`.size()` | O(1) |
|`.search()` | O(n) |
|`.remove()` | O(n) |
|`.display()` | O(n) |

***

### Doubly Linked List
Type of Linked list, there are two references associated with each node, 
One of the reference points to the next node and one to the previous node.
[[3]](http://www.geeksforgeeks.org/overview-of-data-structures-set-1-linear-data-structures/)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.push()` | O(1) |
|`.append()` | O(1) |
|`.pop()` | O(1) |
|`.shift()` | O(1) |
|`.display()` | O(n) |
|`.size()` | O(1) |

***

### Stack (last in, first out)
Abstract data type that serves as a collection of elements, with two principal operations: 
**push**, which adds an element to the collection, and **pop**, 
which removes the last element that was added. In stack both the operations 
of push and pop takes place at the same end that is top of the stack.
[[4]](http://www.geeksforgeeks.org/overview-of-data-structures-set-1-linear-data-structures/)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.push()` | O(1) |
|`.pop()` | O(1) |
|`.len()` | O(1) |

***

### Queue (first in, first out) 
Abstract data type that serves as a collection of elements, 
with two principal operations: **enqueue**, the process of adding an 
element to the collection, and **dequeue**, the process of removing the 
first element that was added.
[[5]](http://www.geeksforgeeks.org/overview-of-data-structures-set-1-linear-data-structures/)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.enqueue()` | O(1) |
|`.dequeue()` | O(1) |
|`.peek()` | O(1) |
|`.size()` | O(1) |

***

### Deque (Double-Ended Queue)
Abstract data type that generalizes a queue, 
for which elements can be added to or removed from either the front or back.
[[6]](https://en.wikipedia.org/wiki/Double-ended_queue)

**Time Complexity**

| Method | Front/Back | Big O |
|--------|:-----:|-------|
|`.append()` | Back | O(1) |
|`.appendleft()` | Front | O(1) |
|`.pop()` | Back | O(1) |
|`.popleft()` | Front | O(1) |
|`.peek()` | Back | O(1) |
|`.peekleft()` | Front | O(1) |
|`.size()` | N/A | O(1) |

***

### Priority Queue
Abstract data type which is like a regular queue or stack data structure, 
but where additionally each element has a "priority" associated with it. 
In a priority queue, an element with high priority is served before an 
element with low priority. If two elements have the same priority, 
they are served according to their order in the queue.
[[7]](https://en.wikipedia.org/wiki/Priority_queue)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.insert()` | O(1) |
|`.pop()` | O(1) |
|`.peek()` | O(1) |

***

### Binary Heap
A tree-type data structure with two main properties:

**Shape property**: The tree is mostly complete with only the deepest level left unfilled

**Heap property**: The heap property has two modes dictating relationships between parent and child nodes:
- Max Heap: Each node is greater than or equal to its child nodes
- Min Heap: Each node is less than or equal to its child nodes

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.push()` | O(n) |
|`.pop()` | O(n) |

***

### Binary Search Tree
Tree data structure in which each node has at most two children, 
which are referred to as the left child and the right child.
[[8]](https://en.wikipedia.org/wiki/Binary_tree)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.insert()` | O(log(n)) |
|`.search()` | O(log(n)) |
|`.depth()` | O(1) |
|`.size()` | O(1) |
|`.contains()` | O(log(n)) |
|`.balance` | O(1) |

***

### Graph
An abstract data type that is meant to implement the directed graph concept from mathematics, 
specifically the field of graph theory.

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.nodes()` | O(n) |
|`.edges()` | O(1) |
|`.add_node()` | O(1) |
|`.add_edge()` | O(1) |
|`.del_node()` | O(n) |
|`.del_edge()` | O(n) |
|`.has_node()` | O(1) |
|`.neighbors()` | O(1) |
|`.adjacent()` | O(n) |

***

### Trie Tree
A kind of search tree—an ordered tree data structure that is used to 
store a dynamic set or associative array where the keys are usually strings.
[[9]](https://en.wikipedia.org/wiki/Trie)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.insert()` | O(log(n)) |
|`.contains()` | O(log(n)) |
|`.size()` | O(1) |
|`.remove()` | O(1) |

***

### Hash Table
A Hash Table is is a data structure which implements an associative array abstract data type, 
a structure that can map keys to values. 

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.get()` | O(log(n)) |
|`.set()` | O(1) |
|`.hash()` | O(1) |

***

## Sorting Algorithms

A sorting algorithm is an algorithm that puts elements of a list in a certain order. 
Efficient sorting is important for optimizing the use of other algorithms 
(such as search and merge algorithms) which require input data to be in sorted lists; 
it is also often useful for canonicalizing data and for producing human-readable output.
[[10]](https://en.wikipedia.org/wiki/Sorting_algorithm)

***

### Bubble Sort
Simple sorting algorithm that repeatedly steps through the list to be sorted, 
compares each pair of adjacent items and swaps them if they are in the wrong order.
[[11]](https://en.wikipedia.org/wiki/Bubble_sort)

**Steps**

- Start at the beginning of the data set 
- Compare the first two elements
- If the first is greater than the second, swap them
- Continue doing this for each pair of adjacent elements to the end of the data set 
- Start again with the first two elements, repeating until no swaps have occurred on the last pass

**Time Complexity**

|  | Best | Worst | Average |
|------|:----:|:-----:|:-------:|
| **Big O** | O(n) | O(n^2) | O(1) |


***

### Quick Sort
Divide and conquer algorithm which relies on a partition operation: 
to partition an array an element called a pivot is selected.
 All elements smaller than the pivot are moved before it and all greater elements are moved after it.
[[12]](https://en.wikipedia.org/wiki/Quicksort)

**Steps**

- Pick an element, called a pivot, from the array 
- Reorder the array so that all elements with values less than the pivot come before the pivot, 
while all elements with values greater than the pivot come after it
- After this partitioning, the pivot is in its final position
- Recursively apply the above steps to the sub-array of elements with smaller values 
- Separately, recursively apply the above steps to the sub-array of elements with greater values

**Time Complexity**

|  | Best | Worst | Average |
|------|:----:|:-----:|:-------:|
| **Big O** | O(n log(n)) | O(n^2) | O(n^2) |


***

### Insertion Sort
A simple sorting algorithm that works by taking elements from the list 
one by one and inserting them in their correct position into a new sorted list.
[[13]](https://en.wikipedia.org/wiki/Insertion_sort)

**Steps**

- Start iterating at the beginning of the un-sorted list
- Compare the first two elements
- If the first two elements are already in ascending order, the first element is considered to be in 
a sorted sub-list
- Move to next position
- At each position, check the value there against the largest value in the sorted list
- If larger, leave the element in place and moves to the next
- If smaller, insert the element into the correct position within the sorted list


**Time Complexity**

|  | Best | Worst | Average |
|------|:----:|:-----:|:-------:|
| **Big O** | O(n) | O(n^2) | O(n log(n)) |


***

### Merge Sort 
Divide and conquer algorithm that keeps on dividing the list into equal halves until it can no more 
be divided. Then, merge sort combines the smaller sorted lists keeping the new list sorted too.
[[14]](https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)

**Steps**

- Divide the list recursively into two halves until it can no more be divided
- Repeatedly merge sublists to produce new sorted sublists 
- When there is only 1 sublist remaining, this will be the sorted list

**Time Complexity**

|  | Best | Worst | Average |
|------|:----:|:-----:|:-------:|
| **Big O** | O(n log(n)) | O(log(n)) | O(n log(n)) |


***

### Radix Sort
Non-comparative integer sorting algorithm that sorts data with integer 
keys by grouping keys by the individual digits which share the same significant position and value.
[[15]](https://en.wikipedia.org/wiki/Radix_sort)

**Steps**

- Take the least significant digit of each key (1's place)
- Group the keys into buckets based on that digit
- Each bucket preserves the original order of the keys as the keys are dropped into the bucket
- Empty buckets
- Sort by next digit (10's place)
- Repeat until each the digit has been reached

**Time Complexity**

|  | Best | Worst | Average |
|------|:----:|:-----:|:-------:|
| **Big O** | O(n(k)) | O(n(k)) | O(n(k)) |