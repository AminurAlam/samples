class Queue:
    def __init__(self, items = []):
        self.items = items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if len(self.items):
            return self.items.pop(0)
