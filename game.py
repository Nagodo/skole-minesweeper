import pygame
import random

from grid import Grid

game_state = 0

offset = [5, 5]
max_width = 750
tile_size = 20
tile_border_w = (20 * 0.1)
tile_border_offset = tile_border_w / 2
difficulty = 1
textdata = [(32, (-8, -18)),(18, (-5, -10)),(10, (-3, -6)),(8, (-2, -4)),(8, (-2, -4))]

tile_colors = [(0, 0, 0),  (0, 0, 255), (255, 0, 0), (0, 255, 0),(255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

class Game():
    def draw(self):
        if game_state == 0:
            screen.fill((0, 0, 0))
            #Draw title
            font = pygame.font.SysFont('Arial', 50)
            text = font.render('Minesweeper', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (max_width / 2, 100)
            screen.blit(text, textRect)

            #Draw start game text
            font = pygame.font.SysFont('Arial', 30)
            text = font.render('Tryk ENTER for at starte', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (max_width / 2, 200)
            screen.blit(text, textRect)

            #Draw difficulty text
            font = pygame.font.SysFont('Arial', 30)
            text = font.render('Sværhedsgrad: ' + str(difficulty), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (max_width / 2, 300)
            screen.blit(text, textRect)
        
        if game_state == 1:
            for x in range(len(self.grid.grid)):
                for y in range(len(self.grid.grid[x])):
                    if self.grid.grid[x][y].updated:
                        self.grid.grid[x][y].updated = False
                        pygame.draw.rect(screen, (240,240,240,255), pygame.Rect(x * tile_size + offset[0], y * tile_size + offset[1], tile_size, tile_size))
                    
                        if self.grid.grid[x][y].hover:
                            pygame.draw.rect(screen, (159,159,159,255), pygame.Rect(x * tile_size + offset[0] + tile_border_offset, y * tile_size + offset[1] + tile_border_offset, tile_size - tile_border_w, tile_size - tile_border_w))
                        else:
                            pygame.draw.rect(screen, (189,189,189,255), pygame.Rect(x * tile_size + offset[0] + tile_border_offset, y * tile_size + offset[1] + tile_border_offset, tile_size - tile_border_w, tile_size - tile_border_w))

                        if self.grid.grid[x][y].isflagged:
                            pygame.draw.rect(screen, (255,0,0,255), pygame.Rect(x * tile_size + offset[0] + tile_border_offset, y * tile_size + offset[1] + tile_border_offset, tile_size - tile_border_w, tile_size - tile_border_w))

                        if self.grid.grid[x][y].isRevealed:
                            pygame.draw.rect(screen, (219,219,219,255), pygame.Rect(x * tile_size + offset[0] + tile_border_offset, y * tile_size + offset[1] + tile_border_offset, tile_size - tile_border_w, tile_size - tile_border_w))
                            if self.grid.grid[x][y].bombsNear:
                                font = pygame.font.SysFont('Arial', textdata[difficulty-1][0], True)
                                color = tile_colors[self.grid.grid[x][y].bombsNear]
                                text = font.render(str(self.grid.grid[x][y].bombsNear), True, color)
                                screen.blit(text, (x * tile_size + offset[0] + textdata[difficulty-1][1][0] + tile_size / 2, y * tile_size + offset[1] + textdata[difficulty-1][1][1] + tile_size / 2))
                            if self.grid.grid[x][y].isBomb:
                                pygame.draw.circle(screen, (0,0,0,255), (int(x * tile_size + offset[0] + tile_size / 2), int(y * tile_size + offset[1] + tile_size / 2)), int(tile_size / 3))

    def HandleFirstPress(self, x, y):
        self.grid.HandleFirstPress(x, y)               

    def StartGame(self):
        global tile_size
        global game_state
        grid_amount = 15 * difficulty
        SetMaxWidth(difficulty)
        tile_size = (max_width / grid_amount)
        self.grid = Grid(grid_amount, self, difficulty)
        screen.fill((0, 0, 0))
        game_state = 1
    
    def GameOver(self):
        for x in range(len(self.grid.grid)):
            for y in range(len(self.grid.grid[x])):
                self.grid.grid[x][y].isRevealed = True
                self.grid.grid[x][y].updated = True
                    


def SetMaxWidth(difficulty):
    global max_width
    if difficulty == 3:
        max_width = 720
    if difficulty == 4:
        max_width = 840
    if difficulty == 5:
        max_width = 900
    



#Init
pygame.init()
screen = pygame.display.set_mode((1000, 920))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

game_instance = Game()

#Game Loop
running = True
while running:
    #Events
    for event in pygame.event.get():
        #Mouse down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_state == 0:
                game_instance.StartGame()

            if event.key == pygame.K_r and game_state == 1:
                game_state = 0

            if event.key == pygame.K_1 and game_state == 0:
                difficulty = 1
            if event.key == pygame.K_2 and game_state == 0:
                difficulty = 2
            if event.key == pygame.K_3 and game_state == 0:
                difficulty = 3
            if event.key == pygame.K_4 and game_state == 0:
                difficulty = 4
            if event.key == pygame.K_5 and game_state == 0:
                difficulty = 5
       
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == 1:
                for x in range(len(game_instance.grid.grid)):
                    for y in range(len(game_instance.grid.grid[x])):
                        if mouse_x > x * tile_size and mouse_x < x * tile_size + tile_size and mouse_y > y * tile_size and mouse_y < y * tile_size + tile_size:
                            if event.button == 1:
                                game_instance.grid.grid[x][y].OnClick()
                            elif event.button == 3:
                                game_instance.grid.grid[x][y].OnRightClick()
         
                

        if event.type == pygame.QUIT:
            running = False


    #Update
    mouse_pos = pygame.mouse.get_pos()
    
    mouse_x = mouse_pos[0] - offset[0]
    mouse_y = mouse_pos[1] - offset[1]
    if game_state == 1:
        for x in range(len(game_instance.grid.grid)):
            for y in range(len(game_instance.grid.grid[x])):
                if mouse_x > x * tile_size and mouse_x < x * tile_size + tile_size and mouse_y > y * tile_size and mouse_y < y * tile_size + tile_size:
                    game_instance.grid.grid[x][y].hover = True
                    game_instance.grid.grid[x][y].updated = True
                else:
                    if game_instance.grid.grid[x][y].hover:
                        game_instance.grid.grid[x][y].hover = False
                        game_instance.grid.grid[x][y].updated = True
                
            

    game_instance.draw()
    
    pygame.display.flip()
    clock.tick(60)

