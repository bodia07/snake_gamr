from pygame import *

init()
font.init()
mixer.init()



frame_size_x = 720
frame_size_y = 480
#кольори
LIGHTGREEN=(105, 204, 75)
BLACK=(0,0,0)

#фони
FONTNAME = "BCoralPixels-Regular.ttf"
display.set_caption('Snake Eater')
clock = time.Clock()
game_window =display.set_mode((frame_size_x, frame_size_y))

class Label(sprite.Sprite):
    def __init__(self, text, x, y, fontsize=30, color=(225, 228, 232), font_name=FONTNAME):
        super().__init__()
        self.color = color
        self.font = font.Font(FONTNAME, fontsize)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_text(self, new_text, color=(225, 228, 232)):
        self.image = self.font.render(new_text, True, color)

class Snake:




run= True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    game_window.fill(LIGHTGREEN)
    display.update()
    clock.tick(60)
    

