######################################################################################################################################################
################################################################ Game Setup ##########################################################################
######################################################################################################################################################
import pygame
import sys
import random
pygame.init()
clock = pygame.time.Clock()

################################################################ Window Settings #####################################################################
width = 1900
height = 1000
screen = pygame.display.set_mode(
    (width, height))


################################################################ Player 1 ############################################################################
#  .----------------.
# | .--------------. |
# | |      _       | |
# | |     | |      | |
# | |     | |      | |
# | |     | |      | |
# | |     |_|      | |
# | |     (_)      | |
# | '--------------' |
#  '----------------'
# You're not going to belive this, but the model used for the player in the original Pong was just a rectangle! Crazy right! Likewise, our players will be just rectangles.
# player1 = How do you draw a rectangle?
# player1Movement = Bit misleading here, but how fast do you want the player to be going, when its not supposed to be moving?
# player1Speed = Now, how fast do you want it going when it IS supposed to be moving?

################################################################ Player 2 ############################################################################
#  .----------------.
# | .--------------. |
# | |      _       | |
# | |     | |      | |
# | |     | |      | |
# | |     | |      | |
# | |     |_|      | |
# | |     (_)      | |
# | '--------------' |
#  '----------------'
# ctrl+c, ctrl+v. Change it up slightly. Nobody will ever know.

################################################################ Ball ################################################################################
#  .----------------.
# | .--------------. |
# | |      _       | |
# | |     | |      | |
# | |     | |      | |
# | |     | |      | |
# | |     |_|      | |
# | |     (_)      | |
# | '--------------' |
#  '----------------'
# Pong just isn't the same when there's no ball. I'll leave the first line in, because I still find it weird that you need a pyGame rect at this moment, but don't worry, it is right, you can figure out the rest.
ball = pygame.Rect((width/2)-15, (height/2)-15, 30, 30)
# ballStartingSpeed = ???
# ballSpeedX = ???
# ballSpeedY = ???


def ballAnimation():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # What should the ball do if it hits the ceiling?

    # What should the ball do if it hits the floor?

    # What should the ball do if it hits a player?

    # What should the ball do if it hits the wall behing a player?


def ballRestart():
    global ballSpeedX, ballSpeedY

    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # So, the ball has gone out of bounds. What should we do to bring the ball back to the centre of the screen?

    # How should we make the ball start moving straight away (once moved back into the center) to either player?


################################################################ Scores ############################################################################
player1Score = 0
player2Score = 0
gameFont = pygame.font.Font("freesansbold.ttf", 32)

####################################################################################################################################################
################################################################ Game Start ########################################################################
####################################################################################################################################################
while 1:
    for event in pygame.event.get():
        ######################################################## Safe Exit Mechanic ################################################################
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ######################################################## Player movements ######################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Time to make the players move. You'll want to look up pyGame event.type and event.key. Be careful not to mix the two up.
    # Also, be very careful with indentation. Python is unforgiving with this. Why does the indentation work where it does?

    # Player 1

    # Player 2

    # The following will work, once the above has been solved. Simply uncomment and you're good to go!
    # player1.y += player1Movement

    # player2.y += player2Movement

    ######################################################## Player screen boundries ###############################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # You may or may not have seen by now that players can move off the screen. That doesn't sound very fun.
    # How do you restrain both players so that they can only play within the boundries of the screen?
    # HINT: .top and .bottom will help a ton!

    ######################################################## Background Colour and middle line #####################################################
    # Fills in the background a solid black, as well as draws a single line down the middle
    screen.fill((0))
    pygame.draw.aaline(screen, (50, 50, 50), (width/2, 0), (width/2, height))

    ############################################################ Draw Players ######################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Time to draw the players to the screen.
    # Rememeber, they are just rects

    ############################################################ Draw Ball #########################################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # Time to draw the ball to the screen.
    # This time, its not a rect...what is it?

    # Don't forget to call the ball animation, otherwise it might not move!

    ############################################################ Scores and screen Update ##########################################################
    #  .----------------.
    # | .--------------. |
    # | |      _       | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     | |      | |
    # | |     |_|      | |
    # | |     (_)      | |
    # | '--------------' |
    #  '----------------'
    # The font of the game was declared earlier. How do you now print it to the screen with the current scores?

    # Player 1 Score

    # Player 2 Score

    # Updates the screen
    pygame.display.update()

    # Locks the game play rate to 60 fps
    clock.tick(60)
