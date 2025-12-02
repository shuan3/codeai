class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        node=Node(value)
        if not self.root:
            self.root=node
            return self
        tree=self.root
        while True:
            if value<tree.value:
                if not tree.left:
                    tree.left=node
                    return self
                tree=tree.left
            else:
                if not tree.right:
                    tree.right=node
                    return
                tree=tree.right
    def find(self, value):
        if not self.root:
            return False
        tree=self.root
        while tree:
            if value<tree.value:
                tree=tree.left
            elif value>tree.value:
                tree=tree.right
            elif value==tree.value:
                return tree
        return False
    def remove(self, value, current=None, parent=None):
        if not self.root:
            return False
        if not current:
            current=self.root
        while current:
            if value<current.value:
                parent=current
                current=current.left
            elif value>current.value:
                parent=current
                current=current.right
            else:
                if current.left and current.right:
                    successor=self.get_min(current.right)
                    current.value=successor.value
                    self.remove(successor.value, current.right, current)
                elif not parent:
                    if current.left:
                        self.root=current.left
                    else:
                        self.root=current.right
                elif parent.left==current:
                    parent.left=current.left if current.left else current.right
                elif parent.right==current:
                    parent.right=current.left if current.left else current.right
                break
        return self
    def get_min(self, node):
        current=node
        while current.left:
            current=current.left
        return current
    def bfs(self):
        if not self.root:
            return []
        queue=[self.root]
        result=[]
        while queue:
            current=queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result