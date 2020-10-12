class SimpleQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_queue(self):
        return self.items


q = SimpleQueue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.get_queue())
q.dequeue()
print(q.size())
print(q.get_queue())
