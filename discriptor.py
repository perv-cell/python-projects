class DiscriptorDimensions:
    def __set_name__(self,owner,name):
        self.name = f"_{owner.__name__}__"+name      
    def __get__(self, instance, owner):
        return getattr(instance, self.name)  
    def __set__(self,instance,value):
        setattr(instance, self.name ,value)

class DiscriptorDimensions__:
    def __set_name__(self,owner,name):
        self.name = "__"+name     
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self,instance,value):
        setattr(instance, self.name ,value)

class WithDifferentDisc: 
    a = DiscriptorDimensions()
    b = DiscriptorDimensions__()
    def __init__(self, a, b):
        self.a =a 
        self.b =b 

ex = WithDifferentDisc(2,2)
print(ex.__dict__)
print(ex.__b)
try: 
    print(ex.__a)
except:
    print("изменять атрибут __a  даже если кто-то очень захочет невозможно! Только с логикой которая прописана в дескрипторе")    