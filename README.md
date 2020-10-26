# Algorithms and Data Structures
## Data Structures: Five Data Structures every Programmer should know

As computer programmers, we write code to instruct computers to process, store, edit and retrieve data. Data Structure is a method of organizing data so that the information can be stored and retrieved efficiently.

Every computer program needs to store data in various data structures for processing. Modern software programming languages and frameworks are highly advanced that, once common, data structure programming is mostly abstracted behind the scenes to make programmers life easier. Lesser the code complexity, lessen the chances of bugs in it!
Nonetheless, there are instances when we programmers can write more elegant programs and APIs if we know the fundamentals of algorithms and data structures.

Here I am explaining 5 data Structures Every Programmer should know and excel.

# Linked List

Linked lists are the simplest and most common data structures. Linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next.

Links list consist of Nodes and a pointer

Node has a value or data and a pointer which points to the next Node it connects to

## a. Single Linked List

Singly linked lists contain nodes which have a data field as well as a pointer (‘next_node’ in our code below), which points to the next node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and traversal.

## b . Double Linked List

Doubly linked list is a linked data structure that consists of a set of sequentially linked nodes. Each node contains three fields: two link fields (references to the previous and to the next node in the sequence of nodes) and one data field

## Performance of Linked List

Below is the Big O notation performance metrics for Binary tree
 
-----------------------------------
  Access  Search  Insert  Delete  
-----------------------------------
  O(n)    O(n)     O(1)    O(1)    
-----------------------------------


| Acees         | Search        | Insert  |  Delete |
| ------------- |:-------------:| -------:| -------:|
| O(n)     | O(n) | O(1)   | O(1)    |



# 3. Stack

A stack is a data type that serves as a collection of elements which are placed one on top of other, like a stack of plates. 

There are two main operations we can do with a stack
i) push 
ii) pop
i) push
push adds an item to the stack

ii) pop
pop removes the most recently item from the stack.

## Performance of Stack

# 4. Queue

A queue is a collection of items that are maintained in a liner sequence. Items can be added only at one end of the sequence and items can be removed only from the other end of the sequence.

By convention, the end of the sequence at which items are added is called the back, tail, or rear of the queue and the end at which items are removed is called the head or front of the queue. This is exactly analogous to queues where people line up to wait for goods or services.

The operation of adding an item to the rear of the queue is known as enqueue
The operation of removing an element from the front is known as dequeue.
Other operations may also be allowed, often including a peek or front operation that returns the value of the next element to be dequeued without dequeuing it.

The operations of a queue make it a first-in-first-out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.
This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed.


# 5. Tree

Tree data structures look like tree structures. Trees are hierarchical in nature.
Each node in the tree can have one of three states.
It can be a parent node. 
It can be a child node, or it can be both a parent and a child at the same time.
Trees are very familiar to us in the real world like we’re born into a family tree with ancestors and descendants branching out.
Binary trees are a specific type of tree data structure. Binary trees start with a root node and then can contain up to two child nodes, a left and a right. The binary name refers to how the child nodes are limited to two nodes. There’s no limit to how deep the tree hierarchical nodes can go. The real advantage of using a binary tree comes down to how data is added and stored into the tree.

## a .Binary Tree 
## b. Binary search tree (BST)

