from pygame import *
import random
import json 

init()
font.init()
mixer.init()


frame_size_x = 720
frame_size_y = 480


LIGHTGREEN = (105, 204, 75)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)


block_size = 20


FONTNAME = "CoralPixels-Regular.ttf"
score_font = font.Font(FONTNAME, 30)

# Вікно гри
display.set_caption('Snake Eater')
clock = time.Clock()
game_window = display.set_mode((frame_size_x, frame_size_y))

def savescore(score):
    with open('score.json', 'w', encoding='utf-8') as f:
            json.dump({"score":score}, f,ensure_ascii=False)

def loadscore():
    try:
        with open('score.json', 'r', encoding='utf-8') as f:
            score=json.load(f)
            return score["score"]
    except (FileNotFoundError,json.decoder.JSONDecodeError): 
        print("файл не знайдено")
        return 0


class Label(sprite.Sprite):
    def __init__(self, text, x, y, fontsize=30, color=(225, 228, 232), font_name=FONTNAME):
        super().__init__()
        self.color = color
        self.font = font.Font(font_name, fontsize)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_text(self, new_text, color=(225, 228, 232)):
        self.image = self.font.render(new_text, True, color)

class Snake:
    def __init__(self):
        self.body = [[100, 60], [80, 50], [60, 50]]  
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, new_dir):
        opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_dir != opposites.get(self.direction):
            self.change_to = new_dir

    def move(self, food_pos):
        self.direction = self.change_to
        head = self.body[0][:]

        if self.direction == 'UP':
            head[1] -= block_size
        elif self.direction == 'DOWN':
            head[1] += block_size
        elif self.direction == 'LEFT':
            head[0] -= block_size
        elif self.direction == 'RIGHT':
            head[0] += block_size

        self.body.insert(0, head)

        if head == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= frame_size_x or head[1] < 0 or head[1] >= frame_size_y:
            return True
        if head in self.body[1:]:
            return True
        return False
    
    #def check_collision_food(self):

    
    def draw(self, surface):
        for part in self.body:
            draw.rect(surface, BLACK, Rect(part[0], part[1], block_size, block_size))

class Food():
    def __init__(self):
        self.position=[random.randrange(0,frame_size_x,block_size),random.randrange(0,frame_size_y,block_size)]

    def respawn(self):
        self.position=[random.randrange(0,frame_size_x,block_size),random.randrange(0,frame_size_y,block_size)]

    def draw(self,surface):
        draw.rect(surface,RED,Rect(self.position[0], self.position[1], block_size, block_size))

        
    

snake = Snake()
food=Food()
score=0
maxscore=loadscore()
score_lable= Label(f'score:{score}',10,10)
maxscore_lable=Label(f'maxscore:{maxscore}',500,10)


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                snake.change_direction('UP')
            elif e.key == K_DOWN:
                snake.change_direction('DOWN')
            elif e.key == K_LEFT:
                snake.change_direction('LEFT')
            elif e.key == K_RIGHT:
                snake.change_direction('RIGHT')
    

    if snake.move(food.position):
        score+=1
        score_lable.set_text(f'score:{score}')
        food.respawn()
        if score>maxscore:
            maxscore=score
            maxscore_lable.set_text(f'Maxsscore:{maxscore}')
            savescore(maxscore)



    if snake.check_collision():
        run = False

    

    game_window.fill(LIGHTGREEN)
    snake.draw(game_window)
    food.draw(game_window)
    game_window.blit(score_lable.image, score_lable.rect)
    game_window.blit(maxscore_lable.image, maxscore_lable.rect)
    display.update()
    clock.tick(10)

