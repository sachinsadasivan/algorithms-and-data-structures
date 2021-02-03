
class Node(object):

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None

    def get_item(self):
        return self.item

    def get_left(self):
        return self.left

    def set_left(self, item):
        self.left = item

    def get_right(self):
        return self.right

    def set_right(self, item):
        self.right = item

    def get_parent(self):
        return self.parent

    def set_parent(self, item):
        self.parent = item
