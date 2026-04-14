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

key, rt = exp.keyboard.wait()

feedback = stimuli.TextLine("your reaction time is " + str(rt) + " ms")
feedback.present()
exp.clock.wait(3000)
print(rt)

control.end()
