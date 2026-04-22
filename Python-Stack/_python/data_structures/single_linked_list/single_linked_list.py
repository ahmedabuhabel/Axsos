class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current = self.head
        new_node.next = current
        self.head = new_node
        return self

    def print_values(self):
        iterator = self.head
        while iterator != None:
            print(iterator.value)
            iterator = iterator.next
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next
        iterator.next = new_node
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back(
    "fun!"
).print_values()
