import pygame, sys #import statement that imports the pygame 
                   #and sys modules so that our program can 
                   #use the functions in them. All of the 
                   #Pygame functions dealing with graphics, 
                   #sound, and other features that Pygame 
                   #provides are in the pygame module.
                   #When you import the pygame module you 
                   #automatically import all the modules that
                   # are in the pygame module as well, such 
                   # as pygame.images and pygame.mixer.music. 
                   # There’s no need to import these modules-
                   # inside-modules with additional import statements.

from pygame.locals import * # pygame.locals contains several 
                            # constant variables that are easy
                            # to identify as being in the 
                            # pygame.locals module without pygame.

pygame.init() #function call, which always needs to be called 
              # after importing the pygame module and before 
              # calling any other Pygame function.               
              # That it needs to be called first in order 
              # for many Pygame functions to work.

DISPLAYSURF = pygame.display.set_mode((400, 300)) # function, 
# which returns the pygame.Surface object for the window. 
# We pass a tuple value of two integers to the function: (400, 300). 
# This tuple tells the set_mode() function how wide and how 
# high to make the window in pixels. (400, 300) will make a 
# window with a width of 400 pixels and height of 300 pixels.

pygame.display.set_caption('Hello World!') 

while True: # main game loop that has a condition 
# of simply the value True. This means that it never exits due to
# its condition evaluating to False. The only way the program 
# execution will ever exit the loop is if a break statement is 
# executed (which moves execution to the first line after the loop) 
# or sys.exit() (which terminates the program).
    for event in pygame.event.get(): # for loop that will 
# iterate over the list of Event objects that was returned by
# pygame.event.get(). On each iteration through the for loop,
# a variable named event will be assigned the value of the 
# next event object in this list. The list of Event objects 
# returned from pygame.event.get() will be in the order that 
# the events happened. If the user clicked the mouse and then
# pressed a keyboard key, the Event object for the mouse click
# would be the first item in the list and the Event object for 
# the keyboard press would be second. If no events have 
# happened, then pygame.event.get() will return a blank list.
        if event.type == QUIT: #checks if the Event object’s 
# type is equal to the constant QUIT. Remember that since we 
# used the from pygame.locals import * form of the import 
# statement, we only have to type QUIT instead of pygame.locals.QUIT.
            pygame.quit() # is the opposite of the pygame.init() function:
                          # it runs code that deactivates the Pygame library.
            sys.exit()
    pygame.display.update() # draws the Surface object returned 
# by pygame.display.set_mode() to the screen. Since the 
# Surface object hasn’t changed, the same black image is 
# redrawn to the screen each time pygame.display.update() 
# is called.


