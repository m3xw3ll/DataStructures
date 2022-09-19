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