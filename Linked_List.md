# Linked List

A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and
the address of the next node. 
For example,

![](src/linked-list-concept.png)

You have to start somewhere, so we give the address of the first node a special name called HEAD.
Also, the last node in the linked list can be identified because its next portion points to NULL. 

Linked lists can be multiple typles: **singly**, **doubly** and **circular linked list**.

**Linked List Complexity**

Time Complexity

|        | Worst Case | Average Case |
|--------|------------|--------------|
| Search |    O(n)    |     O(n)     |
| Insert |    O(1)    |     O(1)     |
| Delete |    O(1)    |     O(1)     |

Space Complexity ```O(n)```

## Singly Linked List

Each node consists:
- A data item
- An address of another node

The power of a linked list comes form the ability to break the chain and rejoin it. E.g. if you wanted to put an element 
4 between 1 and 2, the steps would be:

- Create a new struct node and allocate memory to it
- Add its data value as 4
- Point its next pointer to the struct node containing 2 as the data value
- Change the next pointer of "1" to the node we just created. 


**Linked list implementation in Python**
```python
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second
    second.next = third

    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
```

## Linked List Operations

There are various linked list operations that allow us to perform different actions on linked lists. The basic linked 
list operations are:
- Traversal
- Insertion
- Deletion
- Search
- Sort

### Traverse a Linked List

Displaying the contents of a linked list is very simple. We keep moving the temp node to the next one and display its
contents. When temp is NULL, we know that we have reached the end of the linked list so we get out of the while loop. 

```python
def print_list(self):
    temp = self.head
    while (temp):
        print(str(temp.data) + " ", end="")
        temp = temp.next
```

### Insert Element to a Linked List

You can add elements to either the beginning, middle or end of a linked list.

#### Insert the the beginning

- Allocate memory for new node
- Store data
- Change next of new node to point to head
- Change head to point to recently created node

```python
def insert_at_beginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
```

#### Insert at the End

- Allocate memory for new node
- Store data
- Traverse to last node
- Change next of last node to recently created node

```python
def insert_at_end(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
        self.head = new_node
        return

    last = self.head
    while (last.next):
        last = last.next

    last.next = new_node
```

#### Insert at the Middle

- Allocate memory and store data for new node
- Traverse to node just before the required position of new node
- Change next pointers to include new node in between

```python
def insert_at_middle(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
    else:
        slow = self.head
        fast = self.head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        new_node.next = slow.next
        slow.next = new_node
```

### Delete from a Linked List

You can delete either from the beginning, end or from a particular position.

#### Delete from beginning

- Point head to the second node

```python
if self.head is None:
    temp = self.head
    self.head = self.head.next
    temp = None
```

#### Delete from end

- Traverse to second last element
- Change its next pointer to NULL

```python
def delete_last(self):
    if self.head is not None:
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            last_node = temp.next
            temp.next = None
            last_node = None
```

#### Delete from middle

- Traverse to element before the element to be deleted
- Change next pointers to exclude the node from the chain

```python
def delete_middle(self):
    if self.head is None or self.head.next is None:
        return

    slow = self.head
    fast = self.head
    prev = None

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
```

### Search an Element in a Linked List

You can search an element in an linked list using a loop using the following steps.

- Make HEAD as the current node
- Run a loop unitl the current node is NULL because the last element points to NULL
- In each interation, check if the key of the node is equal to item. If the key matches the item, return True
otherwise return False
  
```python
def search(self, key):

    current = self.head

    while current is not None:
        if current.data == key:
            return True

        current = current.next

    return False
```

### Sort Elements in a Linked List

We will use the Bubble Sort to sort the elements of a linked list in ascending order.

- Make the HEAD as the current node and create another node index for later use
- If HEAD is NULL, return
- Else, run a loop til the last node (i.e. NULL)
- In each interation, follow the following steps 5-6
- Store the next node of current in index
- Check if the data of the current node is greater than the next node. If its greater swap current and index

```python
def sort_linked_list(self, head):
    current = head
    index = Node(None)

    if head is None:
        return
    else:
        while current is not None:
            # index points to the node next to current
            index = current.next

            while index is not None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data

                index = index.next
            current = current.next
```

### Reverse a Linked List
```python
def reverse(self):
    prev = None
    current = self.head
    next = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev
```

### Remove Duplicates from Linked List
```python
def remove_duplicates(self):
    if self.head is None or self.head.next is None:
        return self.head

    seen = set()

    current = self.head
    seen.add(self.head.data)

    while current.next is not None:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
```

### Delete Nth node from the end of Linked List
````python
def delete_kth_node_from_end(self, n):
    fast = self.head
    slow = self.head

    for _ in range(n):
        fast = fast.next

    if not fast:
        return self.head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
````

### Wrap-Up Singly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def insert_at_middle(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            slow = self.head
            fast = self.head.next

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            new_node.next = slow.next
            slow.next = new_node

    def delete_first(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def delete_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                last_node = temp.next
                temp.next = None
                last_node = None

    def delete_middle(self):
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

    def delete_kth_node_from_end(self, n):
        fast = self.head
        slow = self.head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return self.head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

    def delete_node(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    def sort_linked_list(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def reverse(self):
        prev = None
        current = self.head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return self.head

        seen = set()

        current = self.head
        seen.add(self.head.data)

        while current.next is not None:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    def print_list(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_beginning(2)
    llist.insert_at_beginning(3)
    llist.insert_at_end(4)
    llist.insert_after(llist.head.next, 5)
    llist.insert_at_beginning(10)
    llist.insert_after(llist.head.next, 3)
    llist.insert_at_end(2)

    llist.insert_at_middle(7)

    print('Linked List:')
    llist.print_list()
    print()
    print("After deleting elements:")
    llist.delete_first()
    llist.delete_last()
    llist.delete_middle()
    llist.delete_node(7)
    llist.delete_kth_node_from_end(2)
    print()
    llist.print_list()
    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sort_linked_list(llist.head)
    print("Sorted List: ")
    llist.print_list()
    print()
    print("Reversed List: ")
    llist.reverse()
    llist.print_list()
    print()
    llist.remove_duplicates()
    print("List after removed duplicates: ")
    llist.print_list()
```