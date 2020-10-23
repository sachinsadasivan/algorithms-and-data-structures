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
            print('Root is empty. Setting root to : %s' % node.get_item())
            self.size += 1
        else:  # Otherwise, we need to insert the item into the tree using the binary tree insert algorithm
            print('Root %s is not empty. Need to add %s as a child' % (self.root.get_item(), node.get_item()))
            self.insert(self.root, node)

    def insert(self, parent, child):

        # If child is less than parent, it goes here
        if child.get_item() < parent.get_item():
            print('Child %s is less than parent %s' % (child.get_item(), parent.get_item()))
            if parent.get_left() is None:  # If left node is None (null) we have found our spot!
                print('Left node is %s. So we found our spot. Adding child %s here.' % (parent.get_left(), child.get_item()))
                parent.set_left(child)
                child.set_parent(parent)
                print("%s is the new left of parent %s " % (parent.get_left().get_item(), parent.get_item()))
                print("%s is the new parent of child %s " % (child.get_parent().get_item(), child.get_item()))
                self.size += 1
            # Otherwise we need to call insert again and test for left or right (recursion)
            else:
                print('Left node is %s. So we haven not found our spot yet. Calling recursion to add child %s in the level below here.' % (parent.get_left().get_item(), child.get_item()))
                self.insert(parent.get_left(), child)

        # If child is greater than parent, it goes to the right
        elif child.get_item() > parent.get_item():
            print('Child %s is greater than parent %s' % (child.get_item(), parent.get_item()))
            # If right node is null, we have found our spot!
            if parent.get_right() is None:
                print('Right node is %s. So we found our spot. Adding child %s here.' % (parent.get_right(), child.get_item()))
                parent.set_right(child)
                child.set_parent(parent)
                self.size += 1
            else:
                # Otherwise we need to call insert again and test for left and right using recursion
                print('Right node is %s. So we haven not found our spot yet. Calling recursion to add child %s in the level below here.' % (parent.get_right().get_item(), child.get_item()))
                self.insert(parent.get_right(), child)
        # If the parent and child happen to be equal, we don't do anything assuming that the data in the binary tree is unique

    def does_tree_contains(self, item):
        current_node = self.get_node(item)
        if current_node is None:
            return False
        else:
            return True

    def get_node(self, item):
        current_node = self.root
        while current_node is not None:
            if item == current_node.get_item():
                return current_node
            elif item < current_node.get_item():
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()

        return None

    def delete_item(self, item):
        deleted = False

        # Make sure the root isn't null meaning the tree is empty
        if self.root is None:
            return False

        if self.get_node(item) is None:
            return False

        # Find the node to delete
        node_to_be_deleted = self.get_node(item)
        print("Deleting node %s" % node_to_be_deleted.get_item())

        if node_to_be_deleted is not None:
            # If the node to delete doesn't have any children, just delete it
            if node_to_be_deleted.get_left() is None and node_to_be_deleted.get_right() is None:
                self.unlink_item(node_to_be_deleted, None)
                deleted = True
            # If the node to delete only has a right child, remove it in the h  hierarchy
            elif node_to_be_deleted.get_left() is None and node_to_be_deleted.get_right() is not None:
                self.unlink_item(node_to_be_deleted, node_to_be_deleted.get_right())
                deleted = True
            # If the node to delete only has a left child, remove it in the h  hierarchy
            elif node_to_be_deleted.get_left() is not None and node_to_be_deleted.get_right() is None:
                self.unlink_item(node_to_be_deleted, node_to_be_deleted.get_left())
                deleted = True
            # The node has both children, do a node swap to delete
            else:
                print("Node to be deleted is %s and current root is %s" % (node_to_be_deleted.get_item(), self.root.get_item()))
                print("Left child of %s is %s and Right child of %s is %s" % (node_to_be_deleted.get_item(), node_to_be_deleted.get_left().get_item(), node_to_be_deleted.get_item(), node_to_be_deleted.get_right().get_item()))
                print("Right child of %s is %s and its right child is %s" % (
                node_to_be_deleted.get_item(), node_to_be_deleted.get_right().get_item(), node_to_be_deleted.get_right().get_right().get_item()))

                child = node_to_be_deleted.get_left()
                print("Candidate child node is %s" % child.get_item())
                print("child.get_right() is %s" % child.get_right().get_item())
                print("child.get_left() is %s" % child.get_left().get_item())
                while child.get_right() is not None and child.get_left() is not None:
                    child = child.get_right()
                print("We found the most leaf node %s. We can replace the node to be deleted %s with this node" % (child.get_item(), node_to_be_deleted.get_item()))
                # We have the right most leaf node. We can replace the current node with this node
                child.get_parent().set_right(None)  # Remove the leaf node from it's current position

                child.set_left(node_to_be_deleted.get_left())
                print("Right node of Node t be deleted at this stage is %s" % node_to_be_deleted.get_right().get_item())
                child.set_right(node_to_be_deleted.get_right().get_right())

                self.unlink_item(node_to_be_deleted, child)
                deleted = True
            if deleted:
                self.size -= 1

        return deleted

    def unlink_item(self, node_to_be_deleted, new_node):
        print("node_to_be_deleted is %s" % node_to_be_deleted.get_item())
        print("Unlinking Node: %s" % node_to_be_deleted.get_item())
        if new_node is not None:
            print("New Node is %s" % new_node.get_item())

        if node_to_be_deleted.get_item() == self.root.get_item():
            print("Current Node is Root: %s" % node_to_be_deleted.get_item())
            new_node.set_left(node_to_be_deleted.get_left())
            new_node.set_right(node_to_be_deleted.get_right())
            self.root = new_node
            print("New root is %s. New root left node is %s. New root right node is %s" % (self.root.get_item(), self.root.get_left().get_item(), self.root.get_right().get_item()))
        elif node_to_be_deleted.get_parent().get_right().get_item() == node_to_be_deleted.get_item():
            node_to_be_deleted.get_parent().set_right(new_node)
        else:
            node_to_be_deleted.get_parent().set_left(new_node)

    def display_tree_data(self):

        print("Tree Root is: %s" % self.root.get_item())
        child_node = self.root.get_left()

        print("................... Left side Nodes from tree Root ...................")
        while child_node:
            print("Left child_node is %s" % child_node.get_item())
            if child_node.get_right() is not None:
                print("Right child_node is %s" % child_node.get_right().get_item())
            child_node = child_node.get_left()

        print("................... Right side Nodes from tree Root ...................")
        child_node = self.root.get_right()
        while child_node:
            print("Right child_node is %s" % child_node.get_item())
            if child_node.get_left() is not None:
                print("Left child_node is %s" % child_node.get_left().get_item())
            child_node = child_node.get_right()
