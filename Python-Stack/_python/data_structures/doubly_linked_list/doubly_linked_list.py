class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self
        current = self.head
        self.head = new_node
        new_node.next = current
        current.prev = new_node
        return self

    def insert_specific_position(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self
        current = self.head
        for i in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return self
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = new_node
        new_node.prev = iterator

    def traverse_forward(self):
        iterator = self.head
        while iterator:
            print(iterator.value)
            iterator = iterator.next
        return self

    def traverse_backward(self):
        iterator = self.head
        if iterator is None:
            print("List is empty!")
            return
        while iterator.next:
            iterator = iterator.next
        while iterator:
            print(iterator.value)
            iterator = iterator.prev


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.traverse_forward()
dll.traverse_backward()
