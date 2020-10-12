
class Stack (object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print_items(self):
        print(self.items)


s=Stack()

print(s.is_empty())
s.push(24)


s.push('dog')
print(s.peek())
s.print_items()
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
s.print_items()
print(s.pop())
print(s.pop())
print(s.size())
s.print_items()

