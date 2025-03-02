from pygame import* 
import time as tm
from random import randint 
clock = time.Clock()
mixer.init()

mixer.music.load('blaster.mp3')
fired = mixer.Sound('blaster.mp3')

bg = image.load('galaxy1.jpg')
bg2 = image.load('galaxy1.jpg')
FPS = 60
lost = 0
window_game = display.set_mode((0,0), FULLSCREEN)
w1 , w2 = window_game.get_size()
bg=  transform.scale(image.load('galaxy1.jpg'),(w1,w2))
bg2=  transform.scale(image.load('galaxy1.jpg'),(w1,w2))
bullets = sprite.Group()
points1 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, images, w,h, speed ,x ,y):
        super().__init__()
        self.image = transform.scale(image.load(images),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def risovka(self):
        window_game.blit(self.image, (self.rect.x, self.rect.y))


 
class Player(GameSprite):
    def update(self):
        
        keys = key.get_pressed()
        if keys[K_LEFT] and  self.rect.x >= -1 :
           
                
            self.rect.x -= self.speed

        elif keys[K_RIGHT] and  self.rect.x <= w1-100:


           
                self.rect.x += self.speed
        elif keys[K_UP] and self.rect.y >= 0:
           
                
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y <= w2-100:
            
                
            self.rect.y += self.speed

        elif keys[K_SPACE]:
            self.fire()
            mixer.music.play()
    
    def fire(self):
        bullet = Bullet('T1.png', 50,50  ,15, self.rect.x+6,self.rect.y-30)
        bullet1 = Bullet('T1.png', 50, 50  ,15, self.rect.x+46,self.rect.y-30)
        bullets.add(bullet)
        bullets.add(bullet1)
        
class Bullet(GameSprite):
    def update(self):
         
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()


    



class Enemy(GameSprite):
    def update(self):
        global w1 , w2 
        
        self.rect.y += self.speed
        if self.rect.y > w2:
            self.rect.y = -50
            self.rect.x = randint(0 , w1 )
font.init()
my_font = font.Font("DS Army/DS Army Cyr.ttf",70)

win = my_font.render("YOU WIN!!",True ,(255,0,0))
gg =   Player("ar1.png", 100,100,10,20,20)
y_bg_move = 0 
y_bg2_move = -w2
game = True
ufo1 = Enemy('vrag1.png', 100, 150 , 3, 100, 100)
ufo2 = Enemy('vrag2.png', 100,150 , 3, randint(0,1000), 100)
ufo3 = Enemy('vrag3.png', 100,150 , 3, randint(0,1000), 100)
points = my_font.render("Счёт: 0", True,(255,0,0))
monsters = sprite.Group()

monsters.add(ufo1)
monsters.add(ufo2)
monsters.add(ufo3)

finish = False

while game:
  
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if sprite.groupcollide(bullets, monsters,True,True):
        monsters.add(Enemy("vrag2.png", 100,150,5,randint(0,1000),-10))
        
    
        points1 += 1 
        points = my_font.render("Счёт: "+ str(points1), True,(255,0,0))
    
       
        
        

    if not finish:
        window_game.blit(bg,(0,y_bg_move))
        y_bg_move +=2
        window_game.blit(bg2,(0,y_bg2_move))
        y_bg2_move +=2
        if y_bg_move >= w2:
            y_bg_move = -w2
        if y_bg2_move >= w2:
            y_bg2_move = -w2


        window_game.blit(points,(0,0))
        if points1 >= 5:

            window_game.blit(win,(500,500))
            finish = True
        gg.risovka()
        gg.update()
        monsters.draw(window_game)
        monsters.update()
        bullets.draw(window_game)
        bullets.update()
   
    display.update()
    clock.tick(FPS)
