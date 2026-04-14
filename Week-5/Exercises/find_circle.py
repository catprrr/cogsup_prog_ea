'''
if exp.keyboard.wait(keys = K_a):
    print("You pressed A")
''' #this was bullshit


''' step 1 - import all the relevant packages
remember constants (K_RIGHT, K_LEFT)

2. define:
stimuli
instruction
circle
square
correct
incorrect

3. instruct
present instructions
present stimulus
record key
compare
present feedback'''

from expyriment import design, control, stimuli
from expyriment.misc import geometry
from expyriment.misc.constants import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#object class experiment name
exp = design.Experiment(name = "find_the_circle")
control.set_develop_mode()
control.initialize(exp)

#preload canvas
width, height = exp.screen.size
canvas = stimuli.Canvas(size=(width, height))

# 
circle = stimuli.Circle(
    radius = 50,
    colour=C_BLUE,
    position = (-100, 0))
circle.plot(canvas)

square = stimuli.Rectangle(
    size = 50, 50
)

cue = stimuli.TextLine("press a key")
cue.present()

key = exp.keyboard.wait()
key_text = str(key)

feedback = stimuli.TextLine("you pressed " + key_text)
feedback.present(clear = True, update = True)
exp.clock.wait(3000)
print(key_text)

control.end()
'''
if exp.keyboard.wait(keys = K_a):
    print("You pressed A")
''' #this was bullshit