class Cell:
    reavealed = True
    bomb = True
    def __init__(self, x, y, x_size, y_size):
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
    def draw(self):
        pygame.draw.rect(gameDisplay, red, [x, y, x_size, y_size], width=1)


