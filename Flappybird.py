import pygame
from sys import exit
import time
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_1 = pygame.image.load('graphics/bluebird-downflap.png')

        self.animation_index = 0
        self.image = bird_1
        self.rect = self.image.get_rect(midbottom = (50,250))
        self.gravity =0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE ]:
            self.gravity =-4

    def player_gravity(self):
        self.gravity += 0.2
        self.rect.y += self.gravity 
    
    def player_animation(self):
        if player.animation_index%20 <5  :
            self.image = pygame.image.load('graphics/bluebird-downflap.png')

        elif player.animation_index%20 <= 10 and player.animation_index% 20 > 5 :
            self.image = pygame.image.load('graphics/bluebird-midflap.png')
        
        elif player.animation_index%20 <= 15 and player.animation_index%20 >10  :
            self.image = pygame.image.load('graphics/bluebird-upflap.png')
        
        elif player.animation_index%20 <= 20 and player.animation_index%20 != 20 :
            self.image = pygame.image.load('graphics/bluebird-midflap.png')
    
    def player_collides_boundaries(self):
        if self.rect.y < 0 or self.rect.y > 355:
           return False
        else:
            return True
    
    def player_collides_obstacles(self):
        if player.rect.colliderect(obstacles_1_rect) or player.rect.colliderect(obstacles_2_rect):
            return False
        else:
            return True
     
class Boundaries(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        floor1 = pygame.image.load('graphics/base.png')
        self.floor1_image = floor1
        self.floor1_rect = self.floor1_image.get_rect(bottomleft = (0,500 ))

        floor2 = pygame.image.load('graphics/base.png')
        self.floor2_image = floor2
        self.floor2_rect = self.floor2_image.get_rect(bottomleft = (335,500))
    
    def boundaries_movement(self):
        self.floor1_rect.x -= 1
        self.floor2_rect.x -=1

        if self.floor1_rect.x  <= -335:
            self.floor1_rect.x = 335

        if self.floor2_rect.x  <= -335:
            self.floor2_rect.x = 335

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obstacle_1_image = pygame.image.load('pipe-green.png')
        self.obstacle_1_rect = self.obstacle_1_image.get_rect(midleft = (200,425))

        self.obstacle_2_image = pygame.image.load('pipe-green.png')
        self.obstacle_2_image = pygame.transform.rotate(self.obstacle_2_image,180)
        self.obstacle_2_rect = self.obstacle_2_image.get_rect(midleft = (200,-25))

    def obstacles_movement(self):
        self.obstacle_1_rect.x -= 1
        self.obstacle_2_rect.x -= 1

        if self.obstacle_2_rect.x <= -60 :
            self.obstacle_1_rect.x = 280
            self.obstacle_2_rect.x = 280
            random_num = randint(-100,100 )
            self.obstacle_1_rect.y += random_num
            self.obstacle_2_rect.y += random_num
    
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 


def backgrounds_display(day,bg_day_surf,bg_night_surf):
    if(day):
        return bg_day_surf
    else:  
        return bg_night_surf

#game screen setup
pygame.init()
screen = pygame.display.set_mode((280, 500))
pygame.display.set_caption('flappy bird')
clock = pygame.time.Clock()
game_active = False
bg_timer = 1000
sleep_count = 0

#obstacle display 
obstacles = Obstacles()
obstacles_1_surf = obstacles.obstacle_1_image
obstacles_1_rect = obstacles.obstacle_1_rect

obstacles_2_surf = obstacles.obstacle_2_image
obstacles_2_rect = obstacles.obstacle_2_rect

#seconde screen setup
game_over_surf = pygame.image.load('graphics/gameover.png')
game_over_rect = game_over_surf.get_rect(center  = (140, 80))
message_surf = pygame.image.load('graphics/message.png')
message_rect = message_surf.get_rect(center = (140,250))
sleep_count =0
game_over_count =0


#backgrounds     
current_bg = pygame.image.load('graphics/background-day (1).png')
bg_day_surf = pygame.image.load('graphics/background-day (1).png')
bg_night_surf = pygame.image.load('graphics/background-night.png')
bg_count = 0
day = True

# player setup
player = Player()

#boundaries setup 
boundaries = Boundaries()
player_rect = player.rect


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if(game_active):

        # background control
        screen.blit(current_bg,(0,0))
        bg_timer -= 1
        if(bg_timer <= 0):
            if bg_count%2 == 0 :
                day = True
                bg_timer =1000
                bg_count += 1
                current_bg = backgrounds_display(day,bg_day_surf,bg_night_surf)
            else:
                day = False
                bg_timer =1000
                bg_count += 1
                current_bg = backgrounds_display(day,bg_day_surf,bg_night_surf)
        
        #obstacles display and logic
        obstacles.obstacles_movement()
        screen.blit(obstacles_1_surf,obstacles_1_rect)
        screen.blit(obstacles_2_surf,obstacles_2_rect)
        
        #boundaries display and logics
        boundaries1_surf = boundaries.floor1_image
        boundaries1_rect = boundaries.floor1_rect

        boundaries2_surf = boundaries.floor2_image
        boundaries2_rect = boundaries.floor2_rect

        boundaries.boundaries_movement()

        #player display and logics
        player.player_input()
        player.player_gravity()  
        player.animation_index += 1
        player.player_animation()
        game_active = player.player_collides_boundaries() and player.player_collides_obstacles()
        
        player_surf = player.image
        player_rect = player.rect 

        
        #screen display 
        screen.blit(boundaries1_surf,boundaries1_rect)
        screen.blit(boundaries2_surf,boundaries2_rect)
        screen.blit(player_surf, player_rect) 

        #setting making the bird sleep for one seconde in the seconde screen
        sleep_count =0

    else:
        #setting up the display
        if game_over_count != 0:
            if sleep_count == 0 :
                time.sleep(1)
            sleep_count+= 1
            player_rect.y = 250
            obstacles_1_rect.x = 200
            obstacles_2_rect.x = 200
            screen.fill("beige")
            screen.blit(game_over_surf,game_over_rect)
            screen.blit(message_surf,message_rect)

            
            #returning if space was pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE ]:
                game_active = True
        else:
            sleep_count+= 1
            player_rect.y = 250
            screen.fill("beige")
            screen.blit(message_surf,message_rect)
            
            #returning if space was pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE ]:
                game_active = True
                game_over_count+=1
#bio
    pygame.display.update()
    clock.tick(80)

