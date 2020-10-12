from DataStructures.Tree.node import Node


class BinaryTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size

    def add_item(self, item):
        node = Node(item)

        # If this is first item in the tree , set it as root
        if self.root is None:
            self.root = node
            print('Set root: ' + str(node))
            self.size += 1
        else:  # Otherwise, we need to insert the item into the tree using the binary tree insert algorithm
            self.insert(self.root, node)

    def does_tree_contains(self, item):
        current_node = self.get_node(item)
        if current_node is None:
            return False
        else:
            return True

    def delete_item(self, item):
        deleted = False

        # Make sure the root isn't null meaning the tree is empty
        if self.root is None:
            return False

        # Find the node to delete
        current_node = self.get_node(item)

        if current_node is not None:
            # If the node to delete doesn't have any children, just delete it
            if current_node.get_left() is None and current_node.get_right() is None:
                self.unlink_item(current_node, None)
                deleted = True
            # If the node to delete only has a right child, remove it in the h  hierarchy
            elif current_node.get_left() is None and current_node.get_right() is not None:
                self.unlink_item(current_node, current_node.get_right())
                deleted = True
            # If the node to delete only has a left child, remove it in the h  hierarchy
            elif current_node.get_left() is not None and current_node.get_right() is None:
                self.unlink_item(current_node, current_node.get_left())
                deleted = True
            # The node has both children, do a node swap to delete
            else:
                child = current_node.get_left()
                while child.get_right() is not None and child.get_left() is not None:
                    child = current_node.get_right()

                # We have the right most leaf node. We can replace the current node with this node
                child.get_parent().set_right(None)  # Remove the leaf node from it's current position

                child.set_left(current_node.get_left())
                child.set_right(current_node.get_right())

                self.unlink_item(current_node, child)
                deleted = True
            if deleted:
                self.size -= 1

        return deleted

    def unlink_item(self, current_node, new_node):
        if current_node == self.root:
            new_node.set_left(current_node.get_left())
            new_node.set_right(current_node.get_right())
        elif current_node.get_parent().get_right() == current_node:
            current_node.get_parent().set_right(new_node)
        else:
            current_node.get_parent().set_right(new_node)

    def get_node(self, item):
        current_node = Node(self.root)

        while current_node is not None:
            if item == current_node.get_item():
                return current_node
            elif item < current_node.get_item():
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()

        return None

    def insert(self, parent, child):

        # If child is less than parent, it goes here
        if child.get_item() < parent.get_item():
            if parent.get_left() is None: # If left node is None (null) we have found our spot!
                parent.set_left(child)
                child.set_parent(parent)
                self.size += 1
            # Otherwise we need to call insert again and test for left or right (recursion)
            else:
                self.insert(parent.get_left(), child)

        # If child is greater than parent, it goes to the right
        elif child.get_item() > parent.get_item():
            # If right node is null, we have found our spot!
            if parent.get_right() is None:
                parent.set_right(child)
                child.set_parent(parent)
                self.size += 1
            else:
                self.insert(parent.get_right(), child)
