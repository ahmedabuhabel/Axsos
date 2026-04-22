# Doubly Linked List Implementation in Python

A basic implementation of a **Doubly Linked List (DLL)**. Unlike a Singly Linked List, each node in a DLL contains references to both the **next** node and the **previous** node, allowing for bidirectional traversal.

---

## Features

### 1. `Node` Class

The fundamental building block of the list.

- **`value`**: The data stored in the node.
- **`next`**: Pointer to the subsequent node.
- **`prev`**: Pointer to the preceding node.

### 2. `DoublyLinkedList` Class

The controller class for managing nodes.

- **`append(value)`**: Adds a new node to the end of the list. It automatically handles the `prev` connection to link back to the previous tail.
- **`traverse_forward()`**: Iterates from the `head` to the end of the list, printing values.
- **`traverse_backward()`**: Navigates to the end of the list and then iterates backward to the `head` using the `prev` pointers.

---

## How It Works

In a Doubly Linked List, every addition requires updating two pointers instead of one. This allows you to move backward through the data structure without restarting from the head.

### Example Walkthrough

```python
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

# Forward Traversal Output:
# 10
# 20
# 30

# Backward Traversal Output:
# 30
# 20
# 10
```
