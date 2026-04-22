# Singly Linked List Implementation in Python

A robust implementation of a Singly Linked List data structure in Python, featuring node manipulation, traversal, and advanced deletion logic.

---

## Features

### Data Structures

- **`SLNode`**: A class representing a container for a value and a pointer to the next node.
- **`SList`**: A controller class to manage the sequence of nodes and provide high-level operations.

### Supported Operations

This implementation uses **Method Chaining**, allowing for concise and readable code.

| Category      | Method                | Description                                                 |
| :------------ | :-------------------- | :---------------------------------------------------------- |
| **Insertion** | `add_to_front(val)`   | Inserts a new node at the start of the list.                |
|               | `add_to_back(val)`    | Appends a new node to the end of the list.                  |
| **Deletion**  | `remove_from_front()` | Removes the first node (head) of the list.                  |
|               | `remove_from_back()`  | Removes the last node (tail) of the list.                   |
|               | `remove_val(val)`     | Finds and removes the first occurrence of a specific value. |
| **Utility**   | `print_values()`      | Iterates through the list and prints all node values.       |

---

## Detailed Logic

### Method Chaining

Each method returns `self`, which refers back to the `SList` instance. This allows you to stack operations:

```python
my_list.add_to_front("A").add_to_back("B").remove_from_front()
```
