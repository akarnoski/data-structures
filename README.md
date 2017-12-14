# Data Structures & Algorithms

**Introduction**

In computer science, a data structure is a particular way of organizing 
and storing data in a computer so that it can be accessed and modified 
efficiently. More precisely, a data structure is a collection of data values, 
the relationships among them, and the functions or operations that can be applied 
to the data.[[1]](https://en.wikipedia.org/wiki/Data_structure)

The following data structures are solved using Python by [myself](https://github.com/adriennekarnoski) 
and [Cody Dibble](https://github.com/hcodydibble).


## Getting Started

**Installation:**
- Clone the repository:
- `$ git clone https://github.com/adriennekarnoski/data-structures`
- Move into the **data-structures** directory:
- `$ cd data-structures`
- Start your virtual environment:
- `$ python3 -m venv ENV`
- `$ source bin/ENV/activate`
- Install package
- `$ (ENV) pip install -e .`


## Data Structures

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
|`.search()` | O(N) |
|`.remove()` | O(N) |
|`.display()` | O(N) |


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
|`.display()` | O(N) |
|`.size()` | O(1) |


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


### Binary Heap
A tree-type data structure with two main properties:

**Shape property**: The tree is mostly complete with only the deepest level left unfilled

**Heap property**: The heap property has two modes dictating relationships between parent and child nodes:
- Max Heap: Each node is greater than or equal to its child nodes
- Min Heap: Each node is less than or equal to its child nodes

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.push()` | O(N) |
|`.pop()` | O(N) |


### Binary Search Tree
Tree data structure in which each node has at most two children, 
which are referred to as the left child and the right child.
[[8]](https://en.wikipedia.org/wiki/Binary_tree)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.insert()` | log N |
|`.search()` | log N |
|`.depth()` | O(1) |
|`.size()` | O(1) |
|`.contains()` | log N |
|`.balance` | O(1) |


### Graph
An abstract data type that is meant to implement the directed graph concept from mathematics, 
specifically the field of graph theory.

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.nodes()` | O(N) |
|`.edges()` | O(1) |
|`.add_node()` | O(1) |
|`.add_edge()` | O(1) |
|`.del_node()` | O(N) |
|`.del_edge()` | O(N) |
|`.has_node()` | O(1) |
|`.neighbors()` | O(1) |
|`.adjacent()` | O(N) |


### Trie Tree
A kind of search tree—an ordered tree data structure that is used to 
store a dynamic set or associative array where the keys are usually strings.
[[9]](https://en.wikipedia.org/wiki/Trie)

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.insert()` | log N |
|`.contains()` | log N |
|`.size()` | O(1) |
|`.remove()` | O(1) |


### Hash Table
A Hash Table is is a data structure which implements an associative array abstract data type, 
a structure that can map keys to values. 

**Time Complexity**

| Method | Big O |
|--------|-------|
|`.get()` | log N |
|`.set()` | O(1) |
|`.hash()` | O(1) |


## Sorting Algorithms

### Bubble Sort
### Quick Sort
### Insertion Sort
### Merge Sort 