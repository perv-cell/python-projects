class DiscriptorData:
    def __set_name__(self, owner ,name):
        self.name = "__"+name
    def __get__(self,instance,owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
            
class LinkedList:
    
    def __init__(self,head=None,tail=None):
        self.len_list = 0
        self.head = head if head is not None else None
        self.tail = tail if tail is not None else None
    
    def __call__(self, indx):
        if self.head is None:
            return "Список пуст откуда же там данные"
        index_obj = -1
        dur_obj = self.head
        while dur_obj:
            index_obj+=1
            if indx == index_obj:
                return str(dur_obj)
            dur_obj = dur_obj.next
            
    def __len__(self):
        return self.len_list
    
    def add_obj(self,obj):
        if isinstance(obj, ObjList):
            self.len_list+=1
            if self.head is None:
                self.head = obj
                return 
            if self.tail is None:                
                self.tail = obj
                self.head.next = self.tail
                self.tail.prev = self.head
                return 
            dur_obj = self.tail
            self.tail.next = obj
            self.tail = obj
            self.tail.prev = dur_obj      
            
    def remove_obj(self,indx):
        if self.head is None:
            return None # можно ошибку кинуть чтобы не удаляли несуществующих 
        self.len_list-=1
        index_obj = -1
        dur_obj = self.head
        while dur_obj:
            index_obj+=1
            if indx == index_obj:
                print(dur_obj)
                if dur_obj.prev and dur_obj.next:
                    dur_obj.prev.next = dur_obj.next
                    del dur_obj
                    return index_obj
                if dur_obj.prev:
                    dur_obj.prev.next = None
                    del dur_obj
                    return index_obj
                if dur_obj.next:
                    dur_obj.next.prev = None
                    del dur_obj
                    return index_obj 
                self.tail = None
                self.head = None
            dur_obj = dur_obj.next    
        return index_obj   
        
class ObjList:
    data = DiscriptorData()
    prev = DiscriptorData()
    next = DiscriptorData()
    
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
    def __str__(self):
        return self.data

mylist = LinkedList()
mylist.add_obj(ObjList("sadva"))
mylist.add_obj(ObjList("лала"))
mylist.add_obj(ObjList("ывфлдифы"))
mylist.add_obj(ObjList("фва"))

print(len(mylist))
mylist.remove_obj(1)
print(len(mylist))
print(mylist(2))