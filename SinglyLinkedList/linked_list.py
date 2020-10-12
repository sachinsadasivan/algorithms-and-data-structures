from DataStructures.SinglyLinkedList.node import Node


class LinkedList(object):

    def __init__(self, next_node=None):
        self.next_node = next_node
        self.size = 0

    def get_size(self):
        return self.size

    def get_points_to(self):
        return self.get_points_to

    def add_node(self, data):
        new_node = Node(data, self.next_node)
        self.next_node = new_node
        self.size += 1
        return str(data) + " added to the linked list"

    def print_node(self):
        current_node = self.next_node
        while current_node:
            print (current_node.data)
            current_node = current_node.next_node



my_linked_list = LinkedList()
print ("Inserting data")
print (my_linked_list.add_node(15))
print (my_linked_list.add_node(4))
print (my_linked_list.add_node(26))
print ("Printing Linked List Data")
my_linked_list.print_node()
print ("Size is")
print(my_linked_list.get_size())
print ("Head currenlty is at")
print(my_linked_list.next_node.data)
