"""gravity_assist_intersecting.py

Moon and ship cross orbits and moon slows and turns ship.

Credit: Eric T. Mortenson
"""

from turtle import Shape, Screen, Turtle, Vec2D as Vec
import turtle
import math
import sys

# User input:
G = 8  # Gravitational constant used for the simulation.
NUM_LOOPS = 7000  # Number of time steps in simulation.
Ro_X = -152.18  # Ship starting position x coordinate.
Ro_Y = 329.87  # Ship starting position y coordinate.
Vo_X = 423.10  # Ship translunar injection velocity x component.
Vo_Y = -512.26  # Ship translunar injection velocity y component.


MOON_MASS = 1_250_000

class GravSys():
    """Runs a gravity simulation on n-bodies."""

    
    def __init__(self):
        self.bodies = []
        self.t = 0
        self.dt = 0.001


    def sim_loop(self):
        """Loop bodies in a list through time steps."""
        for index in range(NUM_LOOPS): # stops simulation after while                              
            self.t += self.dt
            for body in self.bodies:
                body.step()

class Body(Turtle):
    """Celestial object that orbits and projects gravity field."""
    def __init__(self, mass, start_loc, vel, gravsys, shape):
        super().__init__(shape=shape)
        self.gravsys = gravsys
        self.penup()
        self.mass=mass
        self.setpos(start_loc)
        self.vel = vel
        gravsys.bodies.append(self)
        self.pendown()  # uncomment to draw path behind object
        
        
    def acc(self):
        """Calculate combined force on body and return vector components."""
        a = Vec(0,0)
        for body in self.gravsys.bodies:
            if body != self:
                r = body.pos() - self.pos()
                a += (G * body.mass / abs(r)**3) * r  # units dist/time^2
        return a
    

    def step(self):
        """Calculate position, orientation, and velocity of a body."""
        dt = self.gravsys.dt
        a = self.acc()
        self.vel = self.vel + dt * a
        xOld, yOld = self.pos()  # for orienting ship
        self.setpos(self.pos() + dt * self.vel)
        xNew, yNew = self.pos()  # for orienting ship
        if self.gravsys.bodies.index(self) == 1:  # the CSM
            dir_radians = math.atan2(yNew-yOld,xNew-xOld)  # for orienting ship
            dir_degrees = dir_radians * 180 / math.pi  # for orienting ship
            self.setheading(dir_degrees+90)  # for orienting ship
            

def main():
    # Setup screen
    screen = Screen()
    screen.setup(width = 1.0, height = 1.0)  # for fullscreen
    screen.bgcolor('black')
    screen.title("Gravity Assist Example")

    # Instantiate gravitational system
    gravsys = GravSys()
    
    # Instantiate Planet
    image_moon = 'moon_27x27.gif'
    screen.register_shape(image_moon)
    moon = Body(MOON_MASS, (-250, 0), Vec(500, 0), gravsys, image_moon)
    moon.pencolor('gray')

    # Build command-service-module (csm) shape
    csm = Shape('compound')
    cm = ((0, 30), (0, -30), (30, 0))
    csm.addcomponent(cm, 'red', 'red')
    sm = ((-60,30), (0, 30), (0, -30), (-60, -30))
    csm.addcomponent(sm, 'red', 'black')
    nozzle = ((-55, 0), (-90, 20), (-90, -20))
    csm.addcomponent(nozzle, 'red', 'red')
    screen.register_shape('csm', csm)

    # Instantiate Apollo 8 CSM turtle
    ship = Body(1, (Ro_X, Ro_Y), Vec(Vo_X, Vo_Y), gravsys, "csm")
    ship.shapesize(0.2)
    ship.color('red')  # path color
    ship.getscreen().tracer(1, 0)
    ship.setheading(90)

    gravsys.sim_loop()

if __name__=='__main__':
    main()

