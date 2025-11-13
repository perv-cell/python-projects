class NewList:
    """ Класс для вычитания списков """
    def __init__(self, *args):
        self.lst = list(*args)
        
    def get_list(self):
        return self.lst
    
    def __sub__(self, other):       
       
        if isinstance(other, NewList):
            list_result = self.sub_lists(self.lst,other.lst)
            return NewList(list_result) 

        if  isinstance(other,list):
            list_result = self.sub_lists(self.lst,other)
            return NewList(list_result)  
        
    def __rsub__(self, other):
        
        if  isinstance(other,list):
            list_result = self.sub_lists(other,self.lst)
            return NewList(list_result)
        
    def __isub__(self, other):
        list_copy = self.lst.copy()

        if isinstance(other, NewList):
            list_result = self.sub_lists(self.lst,other.lst)
            self.lst = list_result      
            return self
        
        if isinstance(other, list):
            list_result = self.sub_lists(self.lst,other)
            self.lst = list_result      
            return self
        
    @staticmethod    
    def sub_lists(lst1, lst2):
        lst2 = [(element, type(element)) for element in lst2]
        return [element for element in lst1 if ((element,type(element)) not in lst2 or lst2.remove((element,type(element))))]

