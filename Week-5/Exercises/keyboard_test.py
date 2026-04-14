from expyriment import design, control, stimuli
from expyriment.misc import geometry
from expyriment.misc.constants import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

exp = design.Experiment(name = "keyboard_test")
control.set_develop_mode()
control.initialize(exp)

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