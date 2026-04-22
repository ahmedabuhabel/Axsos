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

    def remove_from_front(self):
        if self.head == None:
            return self
        self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        if self.head.next == None:
            self.head = None
            return self
        iterator = self.head
        while iterator.next.next != None:
            iterator = iterator.next

        iterator.next = None
        return self

    def remove_val(self, val):
        if self.head == None:
            return self
        if self.head.value == val:
            self.head = self.head.next
            return self
        prev = self.head
        iterator = self.head.next
        while iterator != None:
            if iterator.value == val:
                prev.next = iterator.next
                return self
            prev = iterator
            iterator = iterator.next
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").remove_val(
    "are"
).print_values()
