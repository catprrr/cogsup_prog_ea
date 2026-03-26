# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
from expyriment.misc.constants import *
import math
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

''' PARAMETERS AND CONSTANTS'''

#choose the background and square colour (define before initialising)
colour_options = {
    "1" : C_BLACK,
    "2" : C_BLUE,
    "3" : C_DARKGREY,
    "4" : C_EXPYRIMENT_ORANGE,
    "5" : C_EXPYRIMENT_PURPLE,
    "6" : C_GREEN,
    "7" : C_GREY,
    "8" : C_RED,
    "9" : C_WHITE,
    "10" : C_YELLOW
}

print("1 : black \n2 : blue \n3 : dark grey \n4 : orange \n5 : purple \n6 : green \n7 : grey \n8 : red \n9 : white \n10 : yellow")
bg_col_choice = (input("Choose background colour : ").strip())
sq_col_choice = (input("Choose square colour : ").strip())

#colour definitions
bg_colour = colour_options.get(bg_col_choice, C_WHITE) #background colour
sq_colour = colour_options.get(sq_col_choice, C_BLACK) #square colour


#choose rows and columns
n_rows = int(input("How many rows of squares : "))
n_columns = int(input("How many columns of squares : "))


# choose the square and interval ratio, sizes determine by ratios and screen size
spread = {
    "A" : 5,
    "B" : 3,
    "C" : 2
}

print("A : tight")
print("B : mid")
print ("C : loose")

ratio = input("Define the ratio of interval to square size : ")
int_sq_ratio = spread.get(ratio, 3) #interval:square size


'''
#if experimenter wants to just input choices directly, uncomment this section:
bg_colour = C_WHITE
sq_colour = C_BLACK
n_rows = 5
n_columns = 5
int_sq_ratio = 3

'''
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "herman_grid", background_colour = bg_colour)
control.set_develop_mode()
control.initialize(exp)

#screen size
width, height = exp.screen.size #originally width, height - change back if this doesn't work
border_width = width*0.05 #boundary of the grid in x dimension within the screen
border_height = height*0.05 #boundary of the grid in y dimension within the screen
grid_width = width*0.9
grid_height = height*0.9
#define grid size
grid_boundary = min(grid_width, grid_height) #selects whichever is smaller

# define cell size
cell_width = grid_boundary / n_columns
cell_height = grid_boundary / n_rows

#keep square dimensions by selecting smallest width
cell_size = min(cell_width, cell_height)

# stimuli sizes
squ_size = cell_size * (int_sq_ratio / (int_sq_ratio +1)) #square length
int_size = cell_size * (1 / (int_sq_ratio + 1)) #interval length
canvas = stimuli.Canvas(size=(width, height))


#positions
pos_A1_x = - ((cell_size * n_columns)//2) + cell_size//2
pos_A1_y = (cell_size * n_rows)//2 - cell_size//2

#draw squares

for i in range(n_rows):
    for j in range(n_columns):
        pos_x = - ((cell_size * n_columns)//2) + cell_size//2 + j*cell_size
        pos_y = ((cell_size * n_rows)//2) - cell_size//2 - i*cell_size
        square = stimuli.Rectangle(
            size = (squ_size, squ_size),
            position=(pos_x,pos_y),
            colour=sq_colour)
        square.plot(canvas)


# Start running the experiment
control.start(subject_id=1)

# draw shapes
canvas.present(clear=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()