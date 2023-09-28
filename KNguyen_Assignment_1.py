class Node(object):
    # constructor for Node class
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList(object):
    # constructor for LinkedList class
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0
    
    # add item x to list at index i
    def add(self, i, x):
        if self.size >= self.capacity:
            return False
        if i == 0:
            x.next = self.head
            self.head = x.next
            if self.tail == None:
                self.tail = self.head
        else:
            current = self.head
            for _ in range(i-1):
                current = current.next
            x.prev = current
            x.next = current.next
            if current.next == None:
                self.tail = x
            else:
                current.next.prev = x
            current.next = x
        self.size += 1
        return True
    # remove item at index i from the list
    def remove(self, i):
        if self.head == None:
            return False
        if i == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(i-1):
                current = current.next

class Queue(object):
    
    # constructor for Queue class
    def __init__(self):
        self.linkedList = None
        self.front = None
        self.rear = None

    # adds item to front of queue
    def enqueue(self, x):
        # code goes here
    
    # removes item from rear of queue
    def dequeue(self):
    # code goes here (should return item from end of queue or None if queue is empty)
    
    # returns Boolean of whether queue is currently empty
    def isEmpty(self):
        # code goes here
    
    # returns Boolean of whether queue is currently full
    def isFull(self):
        # code goes here
    
    # clears the queue
    def clear(self):
        # code goes here
    
    # looks at the item at the end of the queue without removing it
    def poll(self):
        # code goes here      


class Stack(object):
    __linkedList = …
    __top = …
    
    # constructor for stack class
    def __init__(self):
        # code goes here

    # push item onto stack
    def push(self, x):
        # code goes here
    
    # pops item from top of stack
    def pop(self):
        # code goes here (should return item from top of stack or None if stack is empty)
    
    # returns Boolean of whether stack is currently empty
    def isEmpty(self):
        # code goes here
    
    # returns Boolean of whether stack is currently full
    def isFull(self):
        # code goes here
    
    # clears the stack
    def clear(self):
        # code goes here
    
    # looks at the top item of the stack without removing it
    def peek(self):
        # code goes here


class StackParenthesesChecker(object):
    __stack = …
    
    # constructor for StackParenthesesChecker class
    def __init__(self):
        # code goes here
    
    # Check if string s has balanced parenthesis
    def isBalanced(self, s):
        # code goes here  


class QueueParenthesesChecker(object):
    __queue1 = …
    __queue2 = …
    
    # constructor for QueueParenthesesChecker class
    def __init__(self):
        # code goes here
    
    # Check if string s has balanced parenthesis
    def isBalanced(self, s):
        # code goes here