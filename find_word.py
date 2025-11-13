import re, string
class Morph:
    def __init__(self, *args):
        self.words = list(args)
    def __eq__(self, other):
        if isinstance(other ,str):
            for word in self.words:               
                if other == word:
                    return True
            return False

    def __ne__(self, other):
        if isinstance(other ,str):
            for word in self.words:               
                if other != word:
                    return True
            return False

text = input() 

dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]
count = 0
for word in text.split():
    for morhp in dict_words:
        if s:= re.sub("[!.,-:;]","", word.strip()).lower() == morhp:
            print(s)
            count+=1
print(count)