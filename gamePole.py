import random
class Cell:
    def __init__(self,around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine 
        self.fl_open = False
class GamePole:
    def __init__(self,N, M):
        self.N = N
        self.M = M
        self.pole = self.init()
        
    def init(self):
        N,M = self.N, self.M
        ready_filed = []
        index_mine = []
        all_index = [i for i in range(N*N)]
        for _ in range(M):
            index_min = random.choice(all_index)
            all_index.remove(index_min)
            index_mine.append(index_min)   
        for row in range(N):
            list_row = []
            for column in range(N):
                index_value = row*N+column
                if index_value in index_mine:
                    list_row.append(
                        Cell(around_mines =
                            self._count_min_around(N,index_value,index_mine),
                            mine = True))
                else:
                    list_row.append(
                        Cell(around_mines =
                            self._count_min_around(N,index_value,index_mine),
                            mine = False))
            ready_filed.append(list_row)
        return ready_filed                
                    
    def _count_min_around(self,size, index, list_index):
        count_around = 0
        if index+size in list_index:
            count_around+=1
        if index-size in list_index:
            count_around+=1 
        if index+1 in list_index:
            count_around+=1
        if index-1 in list_index:
            count_around+=1
        if index+size+1 in list_index:
            count_around+=1
        if index+size-1 in list_index:
            count_around+=1
        if index-size+1 in list_index:
            count_around+=1
        if index-size-1 in list_index:
            count_around+=1
        return count_around
    def show(self):
        show_list = []
        for i in self.pole:
            show_row = []             
            for cell in i:
                if cell.fl_open:
                    if cell.mine:
                        show_row.append("*")
                    else:
                        show_row.append(str(cell.around_mines))   
                else:
                    show_row.append("#")       
            show_list.append(" ".join(show_row))            
        print("\n".join(show_list)) 
             
pole_game = GamePole(10,12)
pole_game.show()