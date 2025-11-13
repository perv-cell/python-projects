class MaxPooling:
    
    def __init__(self, step=None, size=None):
        self.step = step if step is not None else (2, 2)
        self.size = size if size is not None else (2, 2)
        
    
    def __call__(self, matrix):
        self.check_matrix(matrix)
        return self.max_pooling_matrix(matrix)
    
    # если матрица прямоугольная и целочисленная, возвращает maxpooling этой матрицы
    def max_pooling_matrix(self,matrix:list[list[int]]):
        len_vertical = len(matrix)
        len_horizontal = len(matrix[0])
        size_block_vertical = self.size[0]
        size_block_horizontal = self.size[1]

        new_matrix = []
        for i in range(0,len_vertical,self.step[0]):
            max_horizontal = []
            if size_block_vertical > len_vertical  - i:  
                break
            for j in range(0, len_horizontal, self.step[1]):                
                # проверяем всё ли ок у нас с размером блока который будем осматривать
                # если размер который будем обходить по горизонатли больше, просто скипаем и спускаемся на эл ниже
                if size_block_horizontal >  len_horizontal - j:
                    break               
                start_traversing_horizontal = j
                end_traversing_horizontal = j + size_block_horizontal
                
                start_traversing_vertical = i 
                end_traversing_vertical = i + size_block_vertical
                
                big_number = matrix[start_traversing_vertical][start_traversing_horizontal]
                # обходим все индексы, который подподают под размер нашего блока
                for el_vert in range(start_traversing_vertical,end_traversing_vertical):
                    for el_horiz in range(start_traversing_horizontal, end_traversing_horizontal):
                        if matrix[el_vert][el_horiz] > big_number:
                            big_number = matrix[el_vert][el_horiz]
                
                max_horizontal.append(big_number) 
            new_matrix.append(max_horizontal)
        return new_matrix    
    
    # проверяет прямоугольная ли матрица и все ли элементы числа 
    @staticmethod
    def check_matrix(matrix):
        len_vertical = len(matrix)
        index_horizontal = len(matrix[0])
        
        for vertical in matrix:
            if len(vertical) != index_horizontal:
                raise ValueError("Неверный формат для первого параметра matrix.")
                
        for vertical in range(len_vertical):
            for horizontal in range(index_horizontal):
                if not isinstance(matrix[vertical][horizontal], (int,float)):
                    raise ValueError("Неверный формат для первого параметра matrix.")


mp = MaxPooling(step=(1, 1), size=(5, 5))
res = mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]])    # [[88, 88], [76, 78]]
print(res)
