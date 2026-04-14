'''    
display text instruction to press the arrow key corresponding to the position of a circle
present a circle and a square, each on one side of the screen
collect the key press and the reaction time'''


from expyriment import design, control, stimuli

exp = design.Experiment(name="Square+Circle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5, position = (-200, 0))
circle = stimuli.Circle(
    radius=100,
    position = (200, 0))

control.start(subject_id=1)

fixation.present(clear=True, update=True)
exp.clock.wait(500)

square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()=