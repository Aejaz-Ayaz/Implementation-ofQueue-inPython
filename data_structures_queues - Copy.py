
class queue:
    def __init__(self):
        self.items = []
    '''
    All methods takes O(1), except for enqueue which takes O(n)
    '''
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.items == []
