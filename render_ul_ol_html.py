items = ["1" ,"2", "3"]

class RenderList:
    def __init__(self, type_list):
        self.type_list= type_list 
    def __call__(self, lst,*args, **kwargs):
        if self.type_list == "ol":
            open_tags = f"<{self.type_list}>"
            close_tags = f"\n</{self.type_list}>"
        else:
            open_tags = f"<ul>"
            close_tags = f"\n</ul>"
        for string in lst:
            open_tags+=f"\n<li>{string}</li>"
        open_tags+=close_tags
        return open_tags   
    
#tests   
render =  RenderList("ol") 
print(render(items))