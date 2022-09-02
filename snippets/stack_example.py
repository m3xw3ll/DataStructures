class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    # Create an empty stack
    s = Stack()
    print(s)

    # Check if stack is empty
    print(s.isEmpty())

    # Push characters into stack
    chars = ['a', 'b', 'c', 'd']
    for c in chars:
        s.push(c)
    print(s)

    # Remove last character from stack
    s.pop()
    print(s)

    # Just peek into the stack, this won´t remove the character
    s.peek()
    print(s)
