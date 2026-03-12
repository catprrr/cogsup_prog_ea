# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

#Shape parameters

colours = {
    'white':  (255, 255, 255),
    'black':  (0, 0, 0),
    'red':    (255, 0, 0),
    'green':  (0, 128, 0),
    'blue':   (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (128, 0, 128),
    'orange': (255, 165, 0),
    'pink':   (255, 105, 180),
    'cyan':   (0, 255, 255),
    'grey':   (128, 128, 128)
}

shape_names = {3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon', 7: 'heptagon', 8: 'octagon', 10: 'decagon', 12: 'dodecagon'}

#postion constants
positions = [(-100),(100)]

#user inputs

n_stimuli = 2
stimuli_params = []
for i in range(n_stimuli):
    print(f"\nStimuli {i+1}:")
    n_sides = int(input("How many sides? "))
    poly_length = int(input("Side length? "))
    radius = poly_length / (2 * math.sin(math.pi / n_sides))
    poly_position = positions[i]
    colour_name = input("Enter colour (white/black/red/green/blue/yellow/purple/orange/pink/cyan/grey): ")
    poly_colour = colours[colour_name]
    label_text = shape_names.get(n_sides, 'polygon')
    stimuli_params.append((n_sides, poly_length, poly_colour, poly_position, label_text))

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
control.set_develop_mode()
exp = design.Experiment(name = "labelled_shape")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

#Define the functions

def polygon_fun(n_sides, poly_length, poly_colour, poly_position, label_text, clear=False) :
    vertices = geometry.vertices_regular_polygon(n_sides, poly_length)
    top_y = radius
    print(f"n_sides={n_sides}, poly_length={poly_length}, top_y={top_y}")
    polygon = stimuli.Shape(
        vertex_list = vertices,
        colour=poly_colour,
        position = (poly_position, 0))
    
    poly_line = stimuli.Line(
        start_point = (poly_position,top_y),
        end_point = (poly_position,top_y+50),
        line_width=3)
    
    poly_text = stimuli.TextLine(
    text = label_text,
    position = (poly_position, top_y+70),
    text_size = 15,
    text_colour = (255, 255, 255))

    polygon.present(clear=clear, update=False)
    poly_line.present(clear=False, update=False)
    poly_text.present(clear=False, update=False)

# Start running the experiment
control.start(subject_id=1)

#launch function
for i, params in enumerate(stimuli_params):
    clear = (i==0)
    polygon_fun(*params, clear = clear)

exp.screen.update()

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()