# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "labelled_shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#This was to work out sides/lengths of shapes
'''
Triangle with side length 50
Height of equilateral triangle = sqrt(3)/2 * side
tri_height = math.sqrt(3) / 2 * 50
tri_top = tri_height * (2/3)  # top vertex from centre
Hexagon — match triangle height, so radius = tri_height / 2
hex_top = tri_height / 2
'''

# Create a purple equilateral triangle and a regular hexagon separated by 200px distance, and white lines at the top of each shape
triangle = stimuli.Shape(
    vertex_list = geometry.vertices_regular_polygon(3,50),
    colour=(128, 0, 128),
    position =(-100,0))
#print(triangle) #to give co-ordinates of vertices for the lines

hexagon = stimuli.Shape(
    vertex_list = geometry.vertices_regular_polygon(6,25),
    colour=(255, 255, 0),
    position =(100,0))
#print(hexagon)

'''
vertices: [[50, 0], [-25, 43]]; points: [(-25, -22), (25, -22), (0, 21)]
vertices: [[25, 0], [12, 21], [-12, 21], [-25, 0], [-12, -21]]; points: [(-12, -21), (13, -21), (25, 0), (13, 21), (-12, 21), (-24, 0)]
'''

triline = stimuli.Line(
    start_point = (-100,21),
    end_point = (-100,21+50),
    line_width=3)

hexline = stimuli.Line(
    start_point = (100, 21),
    end_point = (100, 21+50),
    line_width=3)

tritext = stimuli.TextLine(
    text = "triangle",
    position = (-100, 21+70),
    text_size = 15,
    text_colour = (255, 255, 255)
)

hextext = stimuli.TextLine(
    text = "hexagon",
    position = (100, 21+70),
    text_size = 15,
    text_colour = (255, 255, 255)
)


# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross and square

triangle.present(clear=True, update=False)
triline.present(clear=False, update=False)
hexline.present(clear=False, update=False)
tritext.present(clear=False, update=False)
hextext.present(clear=False, update=False)
hexagon.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()