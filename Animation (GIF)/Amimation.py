'''
import gizeh
import moviepy.editor as mpy

W,H = 128,128 # width, height, in pixels
duration = 2 # duration of the clip, in seconds

def make_frame(t):
    surface = gizeh.Surface(W,H)
    radius = W*(1+ (t*(duration-t))**2 )/6
    circle = gizeh.circle(radius, xy = (W/2,H/2), fill=(1,0,0)) 
    # xy=(W/x,H/x) Where x is any no. deciding position 
    #fill(,,) combination of one and zero makes different colour
    circle.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("circle.gif",fps=60, opt="OptimizePlus", fuzz=1000)
'''

'''
import numpy as np
import gizeh
import moviepy.editor as mpy

W,H = 1000,1000
duration = 2
ncircles = 20 # Number of circles

def make_frame(t):

    surface = gizeh.Surface(W,H)

    for i in range(ncircles):
        angle = 2*np.pi*(1.0*i/ncircles+t/duration)
        center = W*( 0.5+ gizeh.polar2cart(0.1,angle))
        circle = gizeh.circle(r= W*(1.0-1.0*i/ncircles),
                              xy= center, fill= (i%2,i%2,i%2))
        circle.draw(surface)

    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=duration)
clip.write_gif("loopcircles.gif",fps=15, opt="OptimizePlus", fuzz=10)
'''

'''
import gizeh as gz
import numpy as np
import moviepy.editor as mpy

W = H = 150
D = 2 # duration
nballs=60

# generate random values of radius, color, center
radii = np.random.randint(.1*W,.2*W, nballs)
colors = np.random.rand(nballs,3)
centers = np.random.randint(0,W, (nballs,2))

def make_frame(t):
    surface = gz.Surface(W,H)
    for r,color, center in zip(radii, colors, centers):
        angle = 2*np.pi*(t/D*np.sign(color[0]-.5)+color[1])
        xy = center+gz.polar2cart(W/5,angle) # center of the ball
        gradient = gz.ColorGradient(type="radial",
                     stops_colors = [(0,color),(1,color/10)],
                     xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])
        ball = gz.circle(r=1, fill=gradient).scale(r).translate(xy)
        ball.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("balls.gif",fps=15,opt="OptimizePlus")
'''

'''
import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 1000,500
D = 5 #speed of the ball 
r = 50 # radius of the ball
DJ, HJ = 250, 200 # distance and height of the jumps
ground = 0.75*H # y-coordinate of the ground


gradient = gz.ColorGradient(type="radial",
                stops_colors = [(0,(1,0,0)),(1,(0.1,0,0))],
                xy1=[0.3,-0.3], xy2=[0,0], xy3 = [0,1.4])

def make_frame(t):
    surface = gz.Surface(W,H, bg_color=(1,1,1))
    x = (-W/3)+(5*W/3)*(t/D)
    y = ground - HJ*4*(x % DJ)*(DJ-(x % DJ))/DJ**2
    coef = (HJ-y)/HJ
    shadow_gradient = gz.ColorGradient(type="radial",
                stops_colors = [(0,(0,0,0,.2-coef/5)),(1,(0,0,0,0))],
                xy1=[0,0], xy2=[0,0], xy3 = [0,1.4])
    shadow = (gz.circle(r=(1-coef/4), fill=shadow_gradient)
               .scale(r,r/2).translate((x,ground+r/2)))
    shadow.draw(surface)
    ball = gz.circle(r=1, fill=gradient).scale(r).translate((x,y))
    ball.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("bouncingball.gif",fps=25, opt="OptimizePlus")
'''

'''
import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 1000, 1000
DURATION = 2.0
NDISKS_PER_CYCLE = 8
SPEED = .05

def make_frame(t):

    dt = 1.0*DURATION/2/NDISKS_PER_CYCLE # delay between disks
    N = int(NDISKS_PER_CYCLE/SPEED) # total number of disks
    t0 = 1.0/SPEED # indicates at which avancement to start

    surface = gz.Surface(W,H)
    for i in range(1,N):
        a = (np.pi/NDISKS_PER_CYCLE)*(N-i-1)
        r = np.maximum(0, .05*(t+t0-dt*(N-i-1)))
        center = W*(0.5+ gz.polar2cart(r,a))
        color = 3*((1.0*i/NDISKS_PER_CYCLE) % 1.0,)
        circle = gz.circle(r=0.3*W, xy = center,fill = color,
                              stroke_width=0.01*W)
        circle.draw(surface)
    contour1 = gz.circle(r=.65*W,xy=[W/2,W/2], stroke_width=.5*W)
    contour2 = gz.circle(r=.42*W,xy=[W/2,W/2], stroke_width=.02*W,
                            stroke=(1,1,1))
    contour1.draw(surface)
    contour2.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("shutter.gif",fps=20, opt="OptimizePlus", fuzz=10)
'''

'''
import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 300, 75
D = 2 # duration in seconds
r = 22 # size of the letters / pentagons

gradient= gz.ColorGradient("linear",((0,(0,.5,1)),(1,(0,1,1))),
                           xy1=(0,-r), xy2=(0,r))
shape = gz.regular_polygon(r, 6, stroke_width=3, fill=gradient)

def make_frame(t):
    surface = gz.Surface(W,H, bg_color=(1,1,1))
    for i, letter in enumerate("BHAVIN"):
        angle = max(0,min(1,2*t/D-1.0*i/5))*2*np.pi
        txt = gz.text(letter, "Amiri", 3*r/2, fontweight='bold')
        group = (gz.Group([shape, txt])
                 .rotate(angle)
                 .translate((W*(i+1)/7,H/2)))
        group.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("name.gif",fps=20, opt="OptimizePlus")
'''
'''
import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 500,500
WSQ = W/4 # width of one 'square'
D = 2 # duration
a = np.pi/8 # small angle in one triangle
       # /2 is used for lines  
points = [(0,0),(1,0),(1-np.cos(a)**2,np.sin(2*a)/2),(0,0)]

def make_frame(t):
    surface = gz.Surface(W,H)
    for k, (c1,c2) in enumerate([[(.7,0.05,0.05),(1,0.5,0.5)],
                                [(0.05,0.05,.7),(0.5,0.5,1)]]):

        grad = gz.ColorGradient("linear",xy1=(0,0), xy2 = (1,0),
                               stops_colors= [(0,c1),(1,c2)])
        r = min(np.pi/2,max(0,np.pi*(t-D/3)/D))
        triangle = gz.polyline(points,xy=(-0.5,0.5), fill=grad,
                        angle=r, stroke=(1,1,1), stroke_width=.02)
                                # colour of borders(,,)
        square = gz.Group([triangle.rotate(i*np.pi/2)
                              for i in range(4)])
        squares = (gz.Group([square.translate((2*i+j+k,j))
                            for i in range(-3,4)
                            for j in range(-3,4)])
                   .scale(WSQ)
                   .translate((W/2-WSQ*t/D,H/2)))

        squares.draw(surface)

    return surface.get_npimage()

clip = mpy.VideoClip(make_frame=make_frame).set_duration(D)
clip.write_gif("blueradsquares.gif",fps=15, fuzz=30)
'''


import numpy as np
import gizeh as gz
import moviepy.editor as mpy

W,H = 256,256
R=1.0*W/3
D = 4
yingyang = gz.Group( [
      gz.arc(R,0,np.pi, fill=(0,0,0)),
      gz.arc(R,-np.pi,0, fill=(1,1,1)),
      gz.circle(R/2,xy=(-R/2,0), fill=(0,0,0)),
      gz.circle(R/2,xy=(R/2,0), fill=(1,1,1))])

fractal = yingyang
for i in range(5):
    fractal = gz.Group([yingyang,
                fractal.rotate(np.pi).scale(0.25).translate([R/2,0]),
                fractal.scale(0.25).translate([-R/2,0]),
                gz.circle(0.26*R, xy=(-R/2,0),
                    stroke=(1,1,1), stroke_width=1),
                gz.circle(0.26*R, xy=(R/2,0),
                    stroke=(0,0,0), stroke_width=1)])

# Go one level deep into the fractal
fractal = fractal.translate([(R/2),0]).scale(4)

def make_frame(t):
    surface = gz.Surface(W,H)
    G = 2**(2*(t/D)) # zoom coefficient
    (fractal.translate([R*2*(1-1.0/G)/3,0]).scale(G) # zoom
     .translate(W/2+gz.polar2cart(W/12,2*np.pi*t/D)) # spiral effect
     .draw(surface))
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif("yingyang.gif",fps=15, fuzz=30, opt="OptimizePlus")


