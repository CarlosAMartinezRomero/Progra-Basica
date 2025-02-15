def main():

    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, item):
            self.stack.append(item)

        def pop(self):
            return self.stack.pop() if self.stack else "Pila vacía"

        def display(self):
            return self.stack

    class Queue:
        def __init__(self):
            self.queue = []

        def enqueue(self, item):
            self.queue.append(item)

        def dequeue(self):
            return self.queue.pop(0) if self.queue else "Cola vacía"

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            if not self.head:
                self.head = Node(data)
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

        def display(self):
            elements = []
            current = self.head
            while current:
                elements.append(current.data)
                current = current.next
            return elements

    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Pila:", stack.display())
    print("Pila pop:", stack.pop())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Cola:", queue.queue)
    print("Cola dequeue:", queue.dequeue())

    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    print("Lista Enlazada:", linked_list.display())

main()

    
