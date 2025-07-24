class stack:
    def __init__(self):
        self.items=[]
        
    def push(self, item):
        self.items.append(item) 
    def pop(self):
        self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __repr__(self):
        return str(self.items)
    def clear(self):
        self.items.clear()
    def contains(self, item):
        return item in self.items
    def index(self, item):
        if item in self.items:
            return self.items.index(item)
        return -1
    
stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.push(12)    
stack1.push(23)
print(stack1)
print("popping the last element")
stack1.pop()
print(stack1)
print("peeking the last element")
print(stack1.peek())
print("checking if stack is empty")
print(stack1.is_empty())
print("size of the stack")
print(stack1.size())
print("clearin the stack :")
stack1.clear()
