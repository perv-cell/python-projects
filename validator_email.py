import re
import random
class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None
    
    def _generate_random_email():
        literal = "qwertyuiopasdfghjklzxcvbnm1234567890_"
        host_email = ["@gmail.com","@inbox.ru","@mail.ru"]
        first_part = "".join(random.choice(literal) for _ in range(random.randint(10,15)))
        second_part = random.choice(host_email)
        return first_part+second_part
    
    def __is_email_str(email):
        return isinstance(email,str)
    
    @classmethod
    def get_random_email(cls):
        return cls._generate_random_email()
    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if re.match(r"([A-Za-z0-9]+[.-_]*)+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",email):
            return not re.search(r"\.{2,}",email)
        else:
            return False
        
"""
EmailValidator.check_email("sc_lib@list_ru") == False
EmailValidator.check_email("sc@lib@list_ru") == False 
EmailValidator.check_email("sc.lib@list_ru") == False 
EmailValidator.check_email("sclib@list.ru") == True 
EmailValidator.check_email("sc.lib@listru") == False
EmailValidator.check_email("sc..lib@list.ru") == False"""

print(EmailValidator.check_email("sc_lib@list_ru"))
print(EmailValidator.check_email("sc@lib@list_ru"))
print(EmailValidator.check_email("sc.lib@list_ru"))
print(EmailValidator.check_email("sclib@list.ru"))
print(EmailValidator.check_email("sc.lib@listru"))
print(EmailValidator.check_email("sc..lib@list.ru"))
