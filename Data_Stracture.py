class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# รับเลข 5 ตัวจากผู้ใช้
numbers = []
for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# แสดง Linked List
linked_list = LinkedList()
for num in numbers:
    linked_list.append(num)
print("Linked List:")
linked_list.display()

# แสดง Stack
stack = Stack()
for num in numbers:
    stack.push(num)
print("Stack:")
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()

# แสดง Queue
queue = Queue()
for num in numbers:
    queue.enqueue(num)
print("Queue:")
while not queue.is_empty():
    print(queue.dequeue(), end=" ")
print()

# แสดง Tree
tree_root = TreeNode(numbers[0])
for num in numbers[1:]:
    current = tree_root
    while True:
        if num < current.key:
            if current.left is None:
                current.left = TreeNode(num)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(num)
                break
            else:
                current = current.right

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.key, end=" ")
        in_order_traversal(node.right)

print("Tree (In-order Traversal):")
in_order_traversal(tree_root)
print()

# แสดง Sorting (Bubble Sort)
sorted_numbers = numbers.copy()
bubble_sort(sorted_numbers)
print("Sorting (Bubble Sort):", sorted_numbers)