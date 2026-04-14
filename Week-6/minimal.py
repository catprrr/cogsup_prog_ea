'''    
display text instruction to press the arrow key corresponding to the position of a circle
present a circle and a square, each on one side of the screen
collect the key press and the reaction time

1. add variable collection (just reaction time for now)
2. create a block design that's counterbalanced (deterministic and stochastic - build two blocks
3. then you need to add trials
4. for the stochastic, you need to be able to store the order as a variable 

variables:
subject ID
group (don't need)
block_nb
trial_nb
condition
response
rt
block type : determinisitic or stochastic
circle position : left or right
correct/incorrect : if response matches circle_position
valid/invalid : no response (recorded as None -> for R, we need to store this as "NA" - must be a string)

flipping trials - import random
random.choice(input)
you can have the variable stored

can also have right vs left trials and do shuffle

the table can be stored in R

due the end of the year

working version prior to next session (playing with beta tools (beginner R
1. import file
2. manipulate data arrays
3. plot data visualisation
4. data analysis))
'''


from expyriment import design, control, stimuli, misc

exp = design.Experiment(name="Square+Circle")

# define some constants for the experiment
STIMSIZE = 100 #size of stimuli in pixels
GREY = misc.constants.C_GREY
LATERAL_OFFSET = 300 #offset for lateral positioning

control.set_develop_mode()
control.initialize(exp)


square = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), position = (LATERAL_OFFSET, 0))
circle = stimuli.Circle(radius=STIMSIZE//2, position = (-LATERAL_OFFSET,0))

#preload
square.preload()
circle.preload()

control.start(subject_id=1)

square.present(clear=True, update=False)
circle.present(False, True)
exp.clock.wait(500)

exp.clock.wait(2000)

rt = 2000 #placeholder for reaction time

#add a row of data
exp.data.add([rt]) #add a row of data with RT

control.end()