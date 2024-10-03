class Tile():
    def __init__(self, i, j, game_instance):
        self.game_instance = game_instance
        self.hover = False
        self.isRevealed = False
        self.isBomb = False
        self.bombsNear = 0
        self.updated = True
        self.isflagged = False
        self.x = i
        self.y = j
    
    def OnClick(self):
        if not self.game_instance.grid.firstpress:
            self.game_instance.HandleFirstPress(self.x, self.y)

        if self.isBomb:
            self.game_instance.GameOver()
            return
        
        if self.isflagged:
            return

        self.RevealThis()

    def RevealThis(self):
        self.isRevealed = True
        self.updated = True

        game = self.game_instance

        
        if self.x + 1 < len(game.grid.grid):
            if not game.grid.grid[self.x+1][self.y].isRevealed and not game.grid.grid[self.x+1][self.y].isflagged and not game.grid.grid[self.x+1][self.y].isBomb and not (game.grid.grid[self.x+1][self.y].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                game.grid.grid[self.x+1][self.y].RevealThis()
            
            if self.y + 1 < len(game.grid.grid[self.x+1]):
                if not game.grid.grid[self.x+1][self.y+1].isRevealed and not game.grid.grid[self.x+1][self.y+1].isflagged and not game.grid.grid[self.x+1][self.y+1].isBomb and not (game.grid.grid[self.x+1][self.y+1].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                    game.grid.grid[self.x+1][self.y+1].RevealThis()
            
            if self.y - 1 >= 0:
                if not game.grid.grid[self.x+1][self.y-1].isRevealed and not game.grid.grid[self.x+1][self.y-1].isflagged and not game.grid.grid[self.x+1][self.y-1].isBomb and not (game.grid.grid[self.x+1][self.y-1].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                    game.grid.grid[self.x+1][self.y-1].RevealThis()
        
        if self.x - 1 >= 0:
            if not game.grid.grid[self.x-1][self.y].isRevealed and not game.grid.grid[self.x-1][self.y].isflagged and not game.grid.grid[self.x-1][self.y].isBomb and not (game.grid.grid[self.x-1][self.y].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                game.grid.grid[self.x-1][self.y].RevealThis()
            
            if self.y + 1 < len(game.grid.grid[self.x-1]):
                if not game.grid.grid[self.x-1][self.y+1].isRevealed and not game.grid.grid[self.x-1][self.y+1].isflagged and not game.grid.grid[self.x-1][self.y+1].isBomb and not (game.grid.grid[self.x-1][self.y+1].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                    game.grid.grid[self.x-1][self.y+1].RevealThis()

            if self.y - 1 >= 0:
                if not game.grid.grid[self.x-1][self.y-1].isRevealed and not game.grid.grid[self.x-1][self.y-1].isflagged and not game.grid.grid[self.x-1][self.y-1].isBomb and not (game.grid.grid[self.x-1][self.y-1].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                    game.grid.grid[self.x-1][self.y-1].RevealThis()

        if self.y + 1 < len(game.grid.grid):
            if not game.grid.grid[self.x][self.y+1].isRevealed and not game.grid.grid[self.x][self.y+1].isflagged and not game.grid.grid[self.x][self.y+1].isBomb and not (game.grid.grid[self.x][self.y+1].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                game.grid.grid[self.x][self.y+1].RevealThis()
        
        if self.y - 1 >= 0:
            if not game.grid.grid[self.x][self.y-1].isRevealed and not game.grid.grid[self.x][self.y-1].isflagged and not game.grid.grid[self.x][self.y-1].isBomb and not (game.grid.grid[self.x][self.y-1].bombsNear > 0 and game.grid.grid[self.x][self.y].bombsNear > 0):
                game.grid.grid[self.x][self.y-1].RevealThis()
        
                  

    
    def OnRightClick(self):
        if self.isflagged:
            self.isflagged = False
            self.updated = True
            return
        self.isflagged = True
        self.updated = True