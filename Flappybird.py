import pygame
from sys import exit
import time
from random import randint

class Player():
    def __init__(self):
   
        super().__init__()

        bird_1 = pygame.image.load('graphics/bluebird-downflap.png')
        self.animation_index = 0 #resting the animation index 
        self.image = bird_1
        self.rect = self.image.get_rect(midbottom = (50,250))
        self.gravity =0 #resting the gravity
        self.jump_sound = pygame.mixer.Sound('sounds/flap-101soundboards.mp3')
        self.jump_sound.set_volume(0.2)
   

    def player_input(self,space_pressed, space_handled):
        """ 
            gets the booleans space pressed and space handled
            if space is pressed but not handled the player jumps

        """
        if space_pressed and not space_handled:
            space_handled = True
            self.gravity =-5
            self.jump_sound.play()


    def player_gravity(self):

        """
            increasing the players gravity

        """
        self.gravity += 0.2
        self.rect.y += self.gravity 
    
    def player_animation(self):
        

        """
            changing the player animation by using modulo for cretin time

        """
        if player.animation_index%20 <5  :
            self.image = pygame.image.load('graphics/bluebird-downflap.png')

        elif player.animation_index%20 <= 10 and player.animation_index% 20 > 5 :
            self.image = pygame.image.load('graphics/bluebird-midflap.png')
        
        elif player.animation_index%20 <= 15 and player.animation_index%20 >10  :
            self.image = pygame.image.load('graphics/bluebird-upflap.png')
        
        elif player.animation_index%20 <= 20 and player.animation_index%20 != 20 :
            self.image = pygame.image.load('graphics/bluebird-midflap.png')
    
    def player_collides_boundaries(self):
        """
        returns true if the player collides with the boundaries or false if not
        """
        if self.rect.y < 0 or self.rect.y > 360:
             #setting die sound
            die_sound = pygame.mixer.Sound('sounds/flappy-bird-hit-sound-101soundboards.mp3')
            die_sound.set_volume(0.2)
            die_sound.play()
            return False
        else:
            return True
    
    def player_collides_obstacles(self):
        """
        returns false if the player collides with the obstacles or true if not
        """
        if player.rect.colliderect(obstacles_1_rect) or player.rect.colliderect(obstacles_2_rect):
            #setting die sound
            die_sound = pygame.mixer.Sound('sounds/flappy-bird-hit-sound-101soundboards.mp3')
            die_sound.set_volume(0.2)
            die_sound.play()
            return False
        else:
            return True
    
class Boundaries():
    def __init__(self):
        super().__init__()
        
        floor1 = pygame.image.load('graphics/base.png')
        self.floor1_image = floor1
        self.floor1_rect = self.floor1_image.get_rect(bottomleft = (0,500))

        floor2 = pygame.image.load('graphics/base.png')
        self.floor2_image = floor2
        self.floor2_rect = self.floor2_image.get_rect(bottomleft = (335,500))
    
    def boundaries_movement(self):
        """
            Moves the floor by one pixel for movement illusion

        """
        self.floor1_rect.x -= 1
        self.floor2_rect.x -=1

        if self.floor1_rect.x  <= -335:
            """Moves the floor back if its out of the screen
            """
            self.floor1_rect.x = 335

        if self.floor2_rect.x  <= -335:
            """Moves the floor back if its out of the screen
            """
            self.floor2_rect.x = 335

class Obstacles(pygame.sprite.Sprite):
    """creates the obstacles class
    """
    def __init__(self):
        super().__init__()
        """loading the obstacles images and setting the a rectangle
        """
        self.obstacle_1_image = pygame.image.load('graphics/pipe-green.png')
        self.obstacle_1_rect = self.obstacle_1_image.get_rect(midleft = (200,425))

        self.obstacle_2_image = pygame.image.load('graphics/pipe-green.png')
        self.obstacle_2_image = pygame.transform.rotate(self.obstacle_2_image,180)
        self.obstacle_2_rect = self.obstacle_2_image.get_rect(midleft = (200,-25))

    def obstacles_movement(self):
        """moves the obstacles by one pixel 
        """
        self.obstacle_1_rect.x -= 1
        self.obstacle_2_rect.x -= 1

        if self.obstacle_2_rect.x <= -60:
            """moves the obstacles back to the screen if they are not in the frame
            """
            self.obstacle_1_rect.x = 280
            self.obstacle_2_rect.x = 280
            """adding a random number for the obstacles hight to make the game not repeat itself
            """
            random_num = randint(-125,125)

            self.obstacle_1_rect.y = 275 + random_num
            self.obstacle_2_rect.y = -175 + random_num
    
def score_calc(score):
    """gets the score and adding to it if needed

    Returns:
        score
    """
    if obstacles_1_rect.x == 30:
        """adding to the score if the player jumped between 2 obstacles
        """
        score_sound = pygame.mixer.Sound('sounds/point-101soundboards.mp3')

        """playing score adding sound
        """
        score_sound.set_volume(0.2)
        score_sound.play()

        """adding 1 to the score
        """
        score = score + 1 
    return score

def backgrounds_display(day,bg_day_surf,bg_night_surf):
    """changes the background depends on the time

    Args:
        day : a boolean that calculates if it is day or night
        bg_day_surf : day background
        bg_night_surf : night background

    Returns:
        returns correct background for the time
    """

    if(day):# if it is day
        return bg_day_surf
    else:  
        return bg_night_surf

#game screen setup
pygame.init() #initializing pygame
screen = pygame.display.set_mode((280, 500)) #setting a new screen for display
pygame.display.set_caption('flappy bird') #naming the game  "Flappy bird"
clock = pygame.time.Clock() #setting a new clock
game_active = False #setting a boolean that depends on if the game is active or not 
bg_timer = 1000 #setting a timer that switch the day to night and the opposite
bg_music = pygame.mixer.Sound('sounds/Theme For FlappyBird - Original Track.mp3') #background music
bg_music.set_volume(0.1)
bg_music.play(loops= -1) #looping the music
player = Player()


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
game_over_count =0 #creating a new boolean that count the times the game was played to show the correct starting message


#backgrounds     
current_bg = pygame.image.load('graphics/background-day (1).png')
bg_day_surf = pygame.image.load('graphics/background-day (1).png')
bg_night_surf = pygame.image.load('graphics/background-night.png')
bg_count = 0
day = True

# player setup
player = Player()
space_pressed = False
space_handled = False

#boundaries setup 
boundaries = Boundaries()
player_rect = player.rect

#score counter
font = pygame.font.Font('font/Pixeltype.ttf', 50)
score = 0


while True:
    #starting the game until X mark is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if(game_active):

        # background control
        screen.blit(current_bg,(0,0))
        bg_timer -= 1

        if(bg_timer <= 0):
            #choosing a background depends on the time
            if bg_count%2 == 0 :
                day = True
                bg_timer =2000
                bg_count += 1
                current_bg = backgrounds_display(day,bg_day_surf,bg_night_surf)
            else:
                day = False
                bg_timer =2000
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

        keys = pygame.key.get_pressed()

        #making sure player cant hold the space bar to jump
        if keys[pygame.K_SPACE]:
            if not space_pressed:
                space_pressed = True
                space_handled = False
            else:
                space_handled = True
        else:
            space_pressed = False
            space_handled = False

        player.player_input(space_pressed,space_handled)
        player.player_gravity()  
        player.animation_index += 1 #adding 1 to the animation index to make the player animate
        player.player_animation()
        #stopping the game if the player did not touch the obstacles or boundaries
        game_active = player.player_collides_boundaries() and player.player_collides_obstacles()
        
        player_surf = player.image
        player_rect = player.rect 

        #score counting 
        score = score_calc(score)
        score_surf = font.render(str(score),None,'Black')
        score_rect = score_surf.get_rect(center = (140, 50))

        
        #screen display 
        screen.blit(boundaries1_surf,boundaries1_rect)
        screen.blit(boundaries2_surf,boundaries2_rect)
        screen.blit(player_surf, player_rect) 
        screen.blit(score_surf,score_rect)

    else:

        #setting up the display depends if the game was played more than once 

        if game_over_count != 0: #if it was:
            
            #resting the game
            player_rect.y = 250
            obstacles_1_rect.x = 200
            obstacles_2_rect.x = 200
            
            #creating a game over message
            screen.fill("beige")

            #displaying the score
            score_message_surf = font.render("your score: " + str(score), None, 'Black')
            score_message_rect = score_message_surf.get_rect(center =(140,400))

            #displaying everything on the screen
            screen.blit(game_over_surf,game_over_rect)
            screen.blit(message_surf,message_rect)
            screen.blit(score_message_surf,score_message_rect)

            
            #returning if space was pressed to start again the game
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE ]:
                score = 0
                game_active = True

        else:#if it wasn't:

            #showing the same message but without score and game over texts
            player_rect.y = 250
            screen.fill("beige")
            screen.blit(message_surf,message_rect)
            
            #returning if space was pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE ]:
                game_active = True #starting again the game
                game_over_count+=1 # making sure that the game was played more than once to show the correct starting message

    pygame.display.update()
    clock.tick(90)


