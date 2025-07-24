class queue:
    def __init__ (self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    def is_empty(self):
        return len(self.items) == 0 
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def clear(self):
        self.items.clear()  
    
    
queue1 = queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(12)
queue1.enqueue(23)
print(queue1)
print("dequeueing the first element")
print(queue1.dequeue())
print(queue1)
print("peeking the first element")
print(queue1.peek())
print("checking if queue is empty")
print(queue1.is_empty())
print("size of the queue")
print(queue1.size())
print("clearing the queue:")
queue1.items.clear()      