class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def in_order(self):
        current = self
        stack = []
        res = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif (stack):
                current = stack.pop()
                res.append(current.val)
                current = current.right

            else:
                break
        return res

    def pre_order(self):
        current = self
        stack = []
        res = []
        stack.append(current)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res

    def post_order(self):
        current = self
        last = None
        stack = []
        res = []

        while True:
            if current and current is not last:
                stack.append(current)
                current = current.left
            elif stack:
                tos = stack[-1]
                if tos.right and tos.right is not current:
                    current = tos.right
                else:
                    current = last = stack.pop()
                    res.append(last.val)
            else:
                break
        return res


if __name__ == '__main__':
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)

    print(bst.in_order())
    print(bst.pre_order())
    print(bst.post_order())
