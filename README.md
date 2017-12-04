# data-structures
Code 401: Python Data Structures

## Linked List
Consists of Nodes, each of which contains some data and a pointer to the next node.
### Time Complexity
* push() - O(1)
* pop() - O(1)
* size() - O(1)
* search() - O(N)
* remove() - O(N)
* display() - O(N)


## Stack
Data structure where elements are inserted into and removed from the head of the container.
### Time Complexity
* push() - O(1)
* pop() - O(1)
* len() - O(1)


## Doubly Linked List
Consists of Nodes, each of which contains some data and pointers to the next and previous nodes.
### Time Complexity
* push() - O(1)
* append() - O(1)
* pop() - O(1)
* shift() - O(1)
* display() - O(N)
* size() - O(1)



## Queue
Data structure that inserts elements at the tail and accesses/removes elements at the head.
### Time Complexity
* enqueue() - O(1)
* dequeue() - O(1)
* peek() - O(1)
* size() - O(1)



## Deque
A Queue data structure that works at both ends.
Data can be inserted at the head or tail, and retrieved from the head or the tail.
### Time Complexity
* append() - O(1)
* appendleft() - O(1)
* pop() - O(1)
* popleft() - O(1)
* peek() - O(1)
* peekleft() - O(1)
* size() - O(1)


## Binary Heap
A tree-type data structure with two main properties:
- Shape property: The tree is mostly complete with only the deepest level left unfilled
- Heap property: The heap property has two modes dictating relationships between parent and child nodes
    Max Heap: Each node is greater than or equal to its child nodes
    Min Heap: Each node is less than or equal to its child nodes

### Time Complexity
* push() - O(N)
* pop() - O(N)


## Priority Queue
Addition to a value, each item in the queue has a “priority”.
When an item is popped off of the queue, it returns the highest priority item
### Time Complexity
* insert() - O(1)
* pop() - O(1)
* peek() - O(1)

## Graph
An abstract data type that is meant to implement the directed graph concept from mathematics, specifically the field of graph theory.
### Time Complexity
* nodes() - O(N)
* edges() - O(1)
* add_node() - O(1)
* add_edge() - O(1)
* del_node() - O(N)
* del_edge() - O(N)
* has_node() - O(1)
* neighbors() - O(1)
* adjacent() - O(N)


## Binary Search Tree
A binary search tree is a data structure that allows for fast lookup, addition, and removal of items
### Time Complexity
* insert() - log n
* search() - log n
* depth() - O(1)
* size() - O(1)
* contains() - log n
* balance() - O(1)


## Trie Tree
A Trie Tree is a tree data structure that is used to store an associative array### Time Complexity
* insert() - log n
* contains() - log n
* size() - O(1)
* remove() *in production*
