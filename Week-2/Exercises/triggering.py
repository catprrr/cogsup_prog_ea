# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "launching")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create two squares of red and green separated by 400px distance
red_square = stimuli.Rectangle(size=(50,50), colour=(255, 0, 0), position =(-400,0))
green_square = stimuli.Rectangle(size=(50,50), colour=(0, 128, 0), position =(0,0))

# Start running the experiment
control.start(subject_id=1)

# Present the squares
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)

# The red square moves and the green square moves
for i in range(60):
    red_square.move(offset = (350/60,0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
for i in range(20):
    green_square.move(offset=(350/20,0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)

# Leave it on-screen for 1s
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()