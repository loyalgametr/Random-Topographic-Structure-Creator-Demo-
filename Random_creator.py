# import modules
import random
import plotly.graph_objects as go
import pandas as pd

# DEFINE REQUIRED VARIABLES
will_be_added_list = []  # inside-lists in nested lists
main_list = []
side_y = 30  # also side y determines how big the structure is and changeable
side_x = side_y  # also the max number of inside-lists in nested lists
limited_increase = 3
starting_z_values_of_all_sides = 0  # it is needed without that structure becomes vague

# MAKE SOME SPACE TO MANIPULATE VALUES
for x_elements in range(0, side_x):
    will_be_added_list = []
    for y_elements in range(0, side_y):
        will_be_added_list.append(starting_z_values_of_all_sides)

    main_list.append(will_be_added_list)

loop_index = 1

x_number_index = 1
y_number_index = 1
carry_mountain = 0
carry_sinkhole = 0
random_is_it_mountain = random.randint(0, 9)

if random_is_it_mountain == 2:
    main_list[loop_index][loop_index] = -1 * random.randint(0, limited_increase)
else:
    main_list[loop_index][loop_index] = random.randint(0, limited_increase)

# just the opposite as usual:
# consider lists go like y values are x values for x it is opposite (i.e ex. ot)
# (about plotly library)
"""
    example ot:
    xn
    :
    x2 b  d
    x1 a  c
       y1 y2 y3 .. yn

    means: x indicates the number of inside-lists
    x goes upward in example ot, y goes left to right
    y indicates which element is chosen in chosen list
    main_list[x][y] gives values for ex:
    main_list[x1][y1] = a
"""

# USING SPECIFIED INFORMATION ABOVE, MAKE SOME LOOPS TO MANIPULATE LIST Z
# Considering 2D contour line
while loop_index < side_y / 2:

    x_number_index = loop_index
    y_number_index = loop_index

    max_num_for_approach_in_loop = side_y - loop_index

    positive = 0
    if loop_index == 1:
        if main_list[loop_index][loop_index] > 0:
            positive = 1
            carry_mountain += 1
    else:
        if main_list[loop_index - 1][loop_index - 1] > 0:
            positive = 1
            carry_mountain += 1
        else:
            carry_sinkhole += 1
    # 4 while loops is a loop index
    if loop_index != 1:
        if positive:
            main_list[loop_index][loop_index] = random.randint(main_list[loop_index - 1][loop_index - 1]-1,
                                                main_list[loop_index - 1][loop_index - 1]+limited_increase)
        elif not positive:
            main_list[loop_index][loop_index] = random.randint(main_list
                                                [loop_index - 1][loop_index - 1]-limited_increase,
                                                main_list[loop_index - 1][loop_index - 1]+1)

    while y_number_index - 1 < max_num_for_approach_in_loop:

        n = main_list[loop_index][loop_index]
        m = random.randint(n - 1, n + limited_increase)
        k = random.randint(n - limited_increase, n + 1)

        if positive:
            main_list[x_number_index][y_number_index] = m
        else:
            main_list[x_number_index][y_number_index] = k

        y_number_index += 1

    y_number_index -= 1  # can be complicated but it is the best way I thought
    while x_number_index < max_num_for_approach_in_loop - 1:

        n = main_list[loop_index][loop_index]
        m = random.randint(n - 1, n + limited_increase)
        k = random.randint(n - limited_increase, n + 1)

        x_number_index += 1

        if positive == 1:
            main_list[x_number_index][y_number_index] = m
        else:
            main_list[x_number_index][y_number_index] = k

    while y_number_index > (side_y - max_num_for_approach_in_loop):

        n = main_list[loop_index][loop_index]
        m = random.randint(n - 1, n + limited_increase)
        k = random.randint(n - limited_increase, n + 1)

        y_number_index -= 1

        if positive == 1:
            main_list[x_number_index][y_number_index] = m
        else:
            main_list[x_number_index][y_number_index] = k

    while x_number_index - 1 > (side_y - max_num_for_approach_in_loop):

        n = main_list[loop_index][loop_index]
        m = random.randint(n - 1, n + limited_increase)
        k = random.randint(n - limited_increase, n + 1)

        x_number_index -= 1

        if positive == 1:
            main_list[x_number_index][y_number_index] = m
        else:
            main_list[x_number_index][y_number_index] = k

    loop_index += 1
# END OF THE LIST-Z MANIPULATION FOR MOUNTAIN OR SINKHOLE

# nobody is perfect, fixing a small problem (it isn't suppose to occur)
len_will_be_added = len(will_be_added_list)
numbers = 0
while numbers < len(main_list):
    lists = main_list[numbers]
    lists.append(0)
    numbers += 1

# specify if there is a mountain or sinkhole
# the chance of there to be a sinkhole is low like %10
if carry_mountain > carry_sinkhole:
    shape = "mountain"
else:
    shape = "sinkhole"

# if you want to see the list:
# print(main_list)

# making a dictionary to use to make a mountain
"""(because of plotly and pandas libraries dictionary is needed to 
    evaluate values in functions like go.Surface() )"""
my_z_dict = {}

z = main_list
elements = 1

# filling up my_z_dict dictionary to use as our data-z-values (heights)
for lines in z:
    my_z_dict.update({elements: z[elements - 1]})
    elements += 1

# if you want to see defined dictionary:
# print(my_z_dict)

# loading data into a DataFrame object
loaded_z_DataFrame = pd.DataFrame(my_z_dict)

# to use modules
fig = go.Figure()

"""you can change its color by just write a color scale on of following:
             'aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
             'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
             'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
             'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
             'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
             'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
             'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
             'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
             'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
             'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
             'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
             'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
             'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
             'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
             'ylorrd'
             like colorscale='speed' below:"""

# using some modules
fig.add_trace(go.Surface(z=loaded_z_DataFrame.values,
                         colorscale='delta'))
# updating plot sizing
fig.update_layout(
    width=1250,
    height=900,
)

# updating 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# adding button
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label=f"3D Surface is:{shape}",
                    method="restyle"
                ),
                dict(
                    args=["type", "contour"],
                    label=f"Contour line is:{shape}",
                    method="restyle"
                )
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

fig.show()
