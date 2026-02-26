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

#Function
def launching_function(temporal_gap, spatial_gap, trigger_speed) :
    for i in range(60):
        red_square.move(offset = ((350-spatial_gap)/60,0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
    exp.clock.wait(temporal_gap)
    for i in range(trigger_speed):
        green_square.move(offset=(350/trigger_speed,0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)

# Launch function
launching_function(1000,50,20)

# Leave it on-screen for 1s
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()


#Combine everything into a single function that displays a horizontal launching event. The function should take parameters that determine:
# whether there is a temporal gap,
# whether there is a spatial gap, and
# whether the second square moves at the same speed as the first square or at a higher speed.
# The program should display the four types of events in succession: Michottean launching, launching with a temporal gap, launching with a spatial gap, and triggering. Save your script as launching_function.py.
