from node import Node
import pdb

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.node_count = 0

    def __repr__(self):
        # iterative in-order traversal
        output_string = ""
        curr_node = self.root
        stack = []
        while True:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            elif stack:
                curr_node = stack.pop()
                output_string += str(curr_node) + " "
                curr_node = curr_node.right
            else:
                break
        return output_string

    def is_empty(self):
        return self.node_count == 0

    def iinsert(self, node):
        node = Node(node)

        if node is None:
            return None

        if self.root is None:
            self.root = node
            self.node_count += 1
            return self.root
        curr_node = self.root
        trailing_node = None

        while curr_node:
            trailing_node = curr_node
            if node.data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if trailing_node is None:
            trailing_node = node
            trailing_node.parent = None
        elif node.data < trailing_node.data:
            trailing_node.left = node
            node.parent = trailing_node
            self.node_count += 1
        else:
            trailing_node.right = node
            node.parent = trailing_node
            self.node_count += 1
        return trailing_node

    def rec_min_value(self, node={}):
        node = self.root if node == {} else node
        if node.left is None:
            return node
        else:
            self.rec_min_value(node.left)

    def rinsert(self, data, root={}):
        root = self.root if root == {} else root

        if root is None:
            temp = Node(data)
            if self.root is None:
                self.root = temp
            self.node_count += 1
            return temp
        if data < root.data:
            root.left = self.rinsert(data, root.left)
        else:
            root.right = self.rinsert(data, root.right)
        self.root = root
        return root

    def rsearch(self, value, root={}):
        root = self.root if root == {} else root
        
        if root is None or root.data == value:
            return root
    
        if root.data < value:
            return self.rsearch(value, root.right)

        return self.rsearch(value, root.left)
        
    def rremove(self, node):
        if node is None:
            return None

        if type(node) is not Node():
            node = self.rsearch(node)
        
        if node.left is None:
            temp = node.right
            node = temp
            return node

        elif node.right is None:
            temp = node.left
            node = temp
            return node

        pdb.set_trace()
        temp = self.rec_min_value(node.right)
        node = temp
        node.right = self.rremove(temp)

        return node



aa = BinarySearchTree()

aa.rinsert(33)
aa.rinsert(34)
aa.rinsert(32)
aa.rinsert(38)
aa.rinsert(37)
aa.rremove(34)
aa.rremove(32)
print(aa)
