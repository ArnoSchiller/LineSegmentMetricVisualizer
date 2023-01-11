import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider

min_x = -5
max_x = 5
min_y = -5
max_y = 5

# base line with length 1 and angle 0 
base_x = [-0.5, 0.5]
base_y = [0.0, 0.0]
base_center_x = np.mean(base_x)
base_center_y = np.mean(base_x)

initLineX = [-0.5, 0.5]
initLineY = [0.0, 0.0]

line_center_x = np.mean(initLineX)
line_center_y = np.mean(initLineY)

def getDescription(cX, cY):
    return "center point: \n ({c_x}, {c_y})\n \n angle: 10".format(
        c_x = round(cX,2), c_y = round(cY,2)) 
    

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = ax.plot(base_x, base_y, lw=2)
line, = ax.plot(initLineX, initLineY, lw=2)
ax.set(xlim=(min_x, max_x), ylim=(min_y, max_y))
# ax.set_xlabel('Time [s]')

# adjust the main plot to make room for the sliders
fig.subplots_adjust(right=0.75, bottom=0.25)

# slider for point 1
axSliderTopLeft = fig.add_axes([0.1, 0.15, 0.3, 0.03])
sliderFirstPoint_x = Slider(
    ax=axSliderTopLeft,
    label='x',
    valmin=min_x,
    valmax=max_x,
    valinit=initLineX[0],
)
axSliderBottomLeft = fig.add_axes([0.1, 0.1, 0.3, 0.03])
sliderFirstPoint_y = Slider(
    ax=axSliderBottomLeft,
    label='y',
    valmin=min_y,
    valmax=max_y,
    valinit=initLineY[0],
)

# slider for point 2
axSliderTopRight = fig.add_axes([0.6, 0.15, 0.3, 0.03])
sliderSecondPoint_x = Slider(
    ax=axSliderTopRight,
    label='x',
    valmin=min_x,
    valmax=max_x,
    valinit=initLineX[1],
)
axSliderBottomRight = fig.add_axes([0.6, 0.1, 0.3, 0.03])
sliderSecondPoint_y = Slider(
    ax=axSliderBottomRight,
    label='y',
    valmin=min_y,
    valmax=max_y,
    valinit=initLineY[1],
)


axDescription = fig.add_axes([0.8, 0.25, 0.15, 0.65])
text = axDescription.text(0, 0, 
    getDescription(cX = line_center_x, cY = line_center_y), 
    ha='left', wrap=True)
axDescription.set_axis_off()

# The function to be called anytime a slider's value changes
def update(val):
    line_x = [sliderFirstPoint_x.val, sliderSecondPoint_x.val]
    line_y = [sliderFirstPoint_y.val, sliderSecondPoint_y.val]

    c_x = np.mean(line_x)
    c_y = np.mean(line_y)
    
    line.set_data(line_x, line_y)
    text.set_text(getDescription(cX=c_x,cY=c_y))
    fig.canvas.draw_idle()


# register the update function with each slider
sliderFirstPoint_x.on_changed(update)
sliderFirstPoint_y.on_changed(update)
sliderSecondPoint_x.on_changed(update)
sliderSecondPoint_y.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    sliderFirstPoint_x.reset()
    sliderFirstPoint_y.reset()
    sliderSecondPoint_x.reset()
    sliderSecondPoint_y.reset()


button.on_clicked(reset)

plt.show()
