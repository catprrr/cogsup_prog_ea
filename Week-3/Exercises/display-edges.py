# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "display_edges")
control.set_develop_mode()
control.initialize(exp)

#shape parameters
width, height = exp.screen.size
pos_width = width//2
pos_height = height//2
side_length = 0.05*width
n_stimuli = 4
pos_TR = ((pos_width-side_length//2),(pos_height-side_length//2))
pos_BR = ((pos_width-side_length//2),(-pos_height+side_length//2))
pos_TL = ((-pos_width+side_length//2),(pos_height-side_length//2))
pos_BL = ((-pos_width+side_length//2),(-pos_height+side_length//2))


#for i in range(n_stimuli):

#def display_edge_function:
square_TR = stimuli.Rectangle(
    size = (side_length, side_length),
    position=pos_TR,
    colour=(255, 0, 0),
    line_width=1)

square_BR = stimuli.Rectangle(
    size = (side_length, side_length),
    position=pos_BR,
    colour=(255, 0, 0),
    line_width=1)

square_TL = stimuli.Rectangle(
    size = (side_length, side_length),
    position=pos_TL,
    colour=(255, 0, 0),
    line_width=1)

square_BL = stimuli.Rectangle(
    size = (side_length, side_length),
    position=pos_BL,
    colour=(255, 0, 0),
    line_width=1)

# Start running the experiment
control.start(subject_id=1)

# plot squares

square_TR.present(clear=True, update=False)
square_BR.present(clear=False, update=False)
square_TL.present(clear=False, update=False)
square_BL.present(clear=False, update=True)



# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()