class HandlerGET:
    
    def __init__(self, func):
        self.__func   =  func
        
    def __call__(self,request):
        m =  request.get("method","GET")
        if m == "GET":
            return self.get(self.__func,request)
        else:   
            return None
               
    def get(self, func, request):
        res = func(request)
        return f"GET:{res}"
    
@HandlerGET # func_decorator = HandlerGET(handler) // __init__ 
def handler(request): 
    return "илья"

res = handler({"method":"GET"}) # func_decorator __call__() не сам handler(), а именно HandlerGET(), а уже внутри HandlerGET мы будет вызывать handler()
print(res)