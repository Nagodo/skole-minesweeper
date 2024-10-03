import random
from tile import Tile

class Grid():
    def __init__(self, amount, game_instance, difficulty):
        self.grid = [[Tile(j, i, game_instance) for i in range(amount)] for j in range(amount)]
        self.firstpress = False
        self.firstpresspos = (0, 0)
        self.difficulty = difficulty
        #Set bombs

    def HandleFirstPress(self, x, y):
        self.firstpress = True
        self.firstpresspos = (x, y)
        self.GenerateBombs(len(self.grid), self.difficulty)

    def GenerateBombs(self, amount, difficulty):
        a = (amount * (difficulty + (difficulty * 2)))
        i = 0
        while i < a:
            i += 1
            x = random.randint(0, amount - 1)
            y = random.randint(0, amount - 1)
            if x == self.firstpresspos[0] or y == self.firstpresspos[1]:
                i -= 1
            else:
                self.grid[x][y].isBomb = True

        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].isBomb:
                    
                    if x-1 >= 0:
                        if not self.grid[x-1][y].isBomb:
                            self.grid[x-1][y].bombsNear += 1
                        
                        if y-1 >= 0:
                            if not self.grid[x-1][y-1].isBomb:
                                self.grid[x-1][y-1].bombsNear += 1

                        if y+1 < len(self.grid[x-1]):
                            if not self.grid[x-1][y+1].isBomb:
                                self.grid[x-1][y+1].bombsNear += 1
                    
                    if y-1 >= 0:
                        if not self.grid[x][y-1].isBomb:
                            self.grid[x][y-1].bombsNear += 1
                    
                    if y+1 < len(self.grid[x]):
                        if not self.grid[x][y+1].isBomb:
                            self.grid[x][y+1].bombsNear += 1

                    if x+1 < len(self.grid):
                        if not self.grid[x+1][y].isBomb:
                            self.grid[x+1][y].bombsNear += 1
                        
                        if y-1 >= 0:
                            if not self.grid[x+1][y-1].isBomb:
                                self.grid[x+1][y-1].bombsNear += 1

                        if y+1 < len(self.grid[x+1]):
                            if not self.grid[x+1][y+1].isBomb:
                                self.grid[x+1][y+1].bombsNear += 1
