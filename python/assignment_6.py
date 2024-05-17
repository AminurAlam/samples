class Queue:
    items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if len(self.items):
            return self.items.pop(0)
