from DataStructures.Tree.binary_tree import BinaryTree

class BinaryTreeTestApp(object):

    def __init__(self):
        print('Testing Binary Tree...')
        self.binary_tree = BinaryTree()
        pass

    def say(self):
        self.binary_tree.add_item(10)
        print(self.binary_tree.get_size())
        self.binary_tree.add_item(20)
        print(self.binary_tree.get_size())
        self.binary_tree.delete_item(20)
        print(self.binary_tree.get_size())


binary_tree_test_app = BinaryTreeTestApp()
binary_tree_test_app.say()