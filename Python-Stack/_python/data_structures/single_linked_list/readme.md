# Singly Linked List Implementation in Python

This project provides a clean and simple implementation of a **Singly Linked List** data structure. It demonstrates node creation, list traversal, and method chaining.

## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
- [Methods](#methods)
- [Usage Example](#usage-example)
- [Time Complexity](#time-complexity)

---

## Overview

A Singly Linked List is a linear collection of data elements called nodes. Each node contains a value and a pointer to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory, making them efficient for certain types of insertions and deletions.

---

## Classes

### 1. `SLNode`

The building block of the list.

- **Attributes**:
  - `value`: The data stored in the node.
  - `next`: A reference to the next node (initially `None`).

### 2. `SList`

The wrapper class that manages the linked nodes.

- **Attributes**:
  - `head`: The starting point of the list (initially `None`).

---

## Methods

This implementation uses **Method Chaining** (returning `self`), allowing you to call multiple methods in a single statement.

| Method              | Description                                                                  |
| :------------------ | :--------------------------------------------------------------------------- |
| `add_to_front(val)` | Adds a new node with the given value to the beginning of the list.           |
| `add_to_back(val)`  | Traverses the list and adds a new node with the given value to the very end. |
| `print_values()`    | Iterates through every node and prints its value to the console.             |

---

## Usage Example

```python
# Create a new list instance
my_list = SList()

# Chain methods to build the list and print results
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

# --- Console Output ---
# Linked lists
# are
# fun!
```
