class Stack:
    
    def __init__(self, top=None):
        self.top = top
    
    def __add__(self, other): 
        stack = Stack(self.top)
        stack.push_back(other)
        return stack
          
    def __iadd__(self, other):
        self.push_back(other)
        return self  # ВАЖНО: возвращаем self
          
    def __mul__(self, others):
        stack = Stack(self.top)
        for other in others:
            stack.push_back(StackObj(other))
        return stack    
    
    def __imul__(self, others):
        for other in others:
            self.push_back(StackObj(other))
        return self  # ВАЖНО: возвращаем self
             
    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current = self.top
            while current.next:
                current = current.next
            current.next = obj
            
    def pop_back(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            removed = self.top
            self.top = None
            return removed
        else:
            current = self.top
            while current.next.next:
                current = current.next
            removed = current.next
            current.next = None
            return removed

    def get_obj(self):
        if self.top is None:
            return []
        
        lst_res = []
        dur_obj = self.top
        while dur_obj:
            lst_res.append(dur_obj.data)
            dur_obj = dur_obj.next
        return lst_res

class Discriptor:
    
    def __set_name__(self, owner, name):        
        self.name = "__"+name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)
    
    def __set__(self,instance,value):
        if isinstance(value, (str, StackObj)): # пока так
            instance.__dict__[self.name] = value
    
class StackObj:
    
    data = Discriptor()
    next = Discriptor()
    
    def __init__(self, data):
        self.data = data
        self.next = None

stack  = Stack()
stack.push_back(StackObj("sdfsd"))
stack = stack * ["dvssd","sdvsd"]
res = stack.get_obj()
print(res)