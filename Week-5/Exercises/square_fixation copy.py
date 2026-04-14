'''    
display text instruction to press the arrow key corresponding to the position of a circle
present a circle and a square, each on one side of the screen
collect the key press and the reaction time'''


from expyriment import design, control, stimuli

exp = design.Experiment(name="Square+Circle")

# define some constants for the experiment
STIMSIZE = 100 #size of stimuli in pixels
GREY = misc.constants.C_GREY
LATERAL_OFFSET = 300 #offset for lateral positioning

control.set_develop_mode()
control.initialize(exp)


square = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE), line_width=5, position = (LATERAL_OFFSET, 0))
circle = stimuli.Circle(size=STIMSIZE//2, position = (-LATERAL_OFFSET,0))

#preload
square.preload()
circle.preload()

control.start(subject_id=1)

square.present(clear=True, update=False)
circle.present(False, True)
exp.clock.wait(500)

exp.clock.wait(2000)

rt = 1000 #placeholder for reaction time

#add a row of data
exp.data.ad([rt]) #add a row of data with RT

control.end()



