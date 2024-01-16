class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if self.is_empty():
            print("Priority Queue Underflow")
            return None
        item = self.queue.pop(0)
        return item[0]

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Circular Queue Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue Underflow")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

# Example usage:
if __name__ == "__main__":
    # Testing Stack implementations
    stack_array = StackArray(5)
    stack_array.push(1)
    stack_array.push(2)
    stack_array.push(3)
    print(stack_array.pop())  # Output: 3
    print(stack_array.peek())  # Output: 2

    stack_linked_list = StackLinkedList()
    stack_linked_list.push(1)
    stack_linked_list.push(2)
    stack_linked_list.push(3)
    print(stack_linked_list.pop())  # Output: 3
    print(stack_linked_list.peek())  # Output: 2

    # Testing Queue implementations
    queue_array = QueueArray(5)
    queue_array.enqueue(1)
    queue_array.enqueue(2)
    queue_array.enqueue(3)
    print(queue_array.dequeue())  # Output: 1

    queue_linked_list = QueueLinkedList()
    queue_linked_list.enqueue(1)
    queue_linked_list.enqueue(2)
    queue_linked_list.enqueue(3)
    print(queue_linked_list.dequeue())  # Output: 1

    # Testing Priority Queue
    priority_queue = PriorityQueue()
    priority_queue.enqueue("Task 1", 3)
    priority_queue.enqueue("Task 2", 1)
    priority_queue.enqueue("Task 3", 2)
    print(priority_queue.dequeue())  # Output: Task 2

    # Testing Circular Queue
    circular_queue = CircularQueue(5)
    circular_queue.enqueue(1)
    circular_queue.enqueue(2)
    circular_queue.enqueue(3)
    print(circular_queue.dequeue())  # Output: 1
