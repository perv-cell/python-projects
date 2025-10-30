import random
class Server:
    """Класс Server выполняет роли отправителя и получателя, то есть мы эмитируем компьютер пользователя"""
    ip = 0
    def __init__(self,routers=None,buffer=None):
        Server.ip+=1
        self.ip = Server.ip
        self.routers = {} if routers is None else routers
        self.buffer = [] if buffer is None else buffer
        #дополнительно можно добавить определитель используемого роутера, у меня же при 
    def send_data(self,data): #отправке сообщения оно отправляется всем роутерам, которые есть у usera         
        if self.routers:
            for value in self.routers.values():
                value.buffer.append(data)
    def get_data(self):
        get_buffer = self.buffer if self.buffer else []
        self.buffer = []
        return get_buffer
    def get_ip(self):
        return self.ip
    
class Router:
    """Класс Router выполняет роль маршрутиризатора"""
    _list_ip_addr = []
    def __init__(self,connections=None):
        self.name = self._generate_ip_addr()
        self.connections = [] if connections is None else connections
        self.buffer = []
    def link(self,server):
        self.connections.append(server)
        server.routers[self.name] = self    
    def unlink(self,server):
        self.connections.remove(server)
        del server.routers[self.name] 
    def send_data(self):
        for data_message in self.buffer:
            for server in self.connections:
                if server.ip == data_message.ip:
                    server.buffer.append(data_message)
                    break
        self.buffer  = []         

    @classmethod
    def _generate_ip_addr(cls):
        ip = []
        for _ in range(4):
            numb = random.randint(100,999)
            ip.append(str(numb))
        ready_ip = ".".join(ip)
        if not(ready_ip in cls._list_ip_addr):
            cls._list_ip_addr.append(ready_ip)
            return ready_ip
        else:
            return cls._generate_ip_addr()
                
class Data:
    """Класс Data для отправки данных пользователем и  успешном получении"""
    def __init__(self,data:str,ip:int):
        self.data = data
        self.ip = ip

router = Router()
s1 = Server()
s2 = Server()
router.link(s1)
router.link(s2)
print(s1.ip)
print(s2.ip)
s1.send_data(Data("привет второму серверу",2))
s2.send_data(Data("привет первому серверу серверу",1))
router.send_data()
print(s1.get_data())
print(s2.get_data())