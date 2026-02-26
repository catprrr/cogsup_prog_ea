# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "square_adj")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create two squares of red and green separated by 200px distance
left_square = stimuli.Rectangle(size=(50,50), colour=(255, 0, 0), position =(100,0))
right_square = stimuli.Rectangle(size=(50,50), colour=(0, 128, 0), position =(-100,0))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross and square

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()