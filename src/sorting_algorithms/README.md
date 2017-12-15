# Data Structures & Algorithms

**Introduction**

The following are the algorithms I've solved using Python, along with a short description and 
their Big O notation.

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