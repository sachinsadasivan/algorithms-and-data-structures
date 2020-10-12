
class Node(object):

    def __init__(self, data=None, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next = next_node

    def __repr__(self):
        return repr(self.data)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.get_next_node

    def get_previous_node(self):
        return self.get_next_node

    def set_next_node(self, previous_node):
        self.previous_node = previous_node
