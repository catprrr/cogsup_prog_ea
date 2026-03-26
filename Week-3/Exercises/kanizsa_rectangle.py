# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
from expyriment.misc.constants import C_WHITE, C_BLACK, C_DARKGREY
import math
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "kanizsa_square", background_colour = C_DARKGREY)
control.set_develop_mode()
control.initialize(exp)

#shape parameters

width, height = exp.screen.size

rect_AR = 3.5
rect_SF = 2
circle_SF = 8


def stimuli_AR(rect_AR, rect_SF, circle_SF):
    rectangle = stimuli.Rectangle(
        size = (squ_side_length, squ_side_length),
        position=(0,0),
        colour=C_DARKGREY)
    

squ_side_length = width*0.25
circle_radius = width*0.05
circle_origin = width*0.125

# draw circles
circle_TL = stimuli.Circle(
    radius=circle_radius,
    colour = C_BLACK,
    position = (-circle_origin, circle_origin)
)

circle_TR = stimuli.Circle(
    radius=circle_radius,
    colour = C_BLACK,
    position = (circle_origin, circle_origin)
)

circle_BL = stimuli.Circle(
    radius=circle_radius,
    colour = C_WHITE,
    position = (-circle_origin, -circle_origin)
)

circle_BR = stimuli.Circle(
    radius=circle_radius,
    colour = C_WHITE,
    position = (circle_origin, -circle_origin)
)

#draw square
central_square = stimuli.Rectangle(
    size = (squ_side_length, squ_side_length),
    position=(0,0),
    colour=C_DARKGREY)


# Start running the experiment
control.start(subject_id=1)

# plot shapes

circle_TL.present(clear=True, update=False)
circle_TR.present(clear=False, update=False)
circle_BL.present(clear=False, update=False)
circle_BR.present(clear=False, update=False)
central_square.present(clear=False, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()