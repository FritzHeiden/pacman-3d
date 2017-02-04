class Stack(object):
    def __init__(self):
        self.items = []

    def clear(self):
        self.items = []

    def peek(self):
        if len(self.items) >= 0:
            return self.items[len(self.items) - 1]
        else:
            return None

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            item = self.items.pop()
            return item
        else:
            return None