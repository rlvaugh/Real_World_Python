from turtle import Shape, Screen, Turtle, Vec2D as Vec

# User input:
G = 8  # Gravitational constant used for the simulation.
NUM_LOOPS = 4100  # Number of time steps in the simulation.
Ro_X = 0  # Ship starting position x coordinate.
Ro_Y = -85  # Ship starting position y coordinate.
Vo_X = 485  # Ship translunar injection velocity x component.
Vo_Y = 0  # Ship translunar injection velocity y component.


class GravSys():
    """Runs a gravity simulation on n-bodies."""
   
    def __init__(self):
        self.bodies = []
        self.t = 0
        self.dt = 0.001                
            
    def sim_loop(self):
        """Loop bodies in a list through time steps."""
        for _ in range(NUM_LOOPS):  # Stops simulation after capsule splashdown.
            self.t += self.dt
            for body in self.bodies:
                body.step()
                

class Body(Turtle):
    """Celestial object that orbits and projects gravity field."""
    def __init__(self, mass, start_loc, vel, gravsys, shape):
        super().__init__(shape=shape)
        self.gravsys = gravsys
        self.penup()
        self.mass = mass
        self.setpos(start_loc)
        self.vel = vel
        gravsys.bodies.append(self)
        #self.resizemode("user")
        #self.pendown()  # Uncomment to draw path behind object.
        
    def acc(self):
        """Calculate combined force on body and return vector components."""
        a = Vec(0, 0)
        for body in self.gravsys.bodies:
            if body != self:
                r = body.pos() - self.pos()
                a += (G * body.mass / abs(r)**3) * r  # Units: dist/time^2.
        return a    
    
    def step(self):
        """Calculate position, orientation, and velocity of a body."""
        dt = self.gravsys.dt
        a = self.acc()
        self.vel = self.vel + dt * a
        self.setpos(self.pos() + dt * self.vel)
        if self.gravsys.bodies.index(self) == 2:  # Index 2 = CSM.
            rotate_factor = 0.0006
            self.setheading((self.heading() - rotate_factor * self.xcor()))
            if self.xcor() < -20:
                self.shape('arrow')
                self.shapesize(0.5)
                self.setheading(105)

    

def main():   
    # Setup screen 
    screen = Screen()
    screen.setup(width=1.0, height=1.0)  # For fullscreen.
    screen.bgcolor('black')
    screen.title("Apollo 8 Free Return Simulation")

    # Instantiate gravitational system
    gravsys = GravSys()

    # Instantiate Earth turtle
    image_earth = 'earth_100x100.gif'
    screen.register_shape(image_earth)
    earth = Body(1000000, (0, -25), Vec(0, -2.5), gravsys, image_earth)
    earth.pencolor('white')
    earth.getscreen().tracer(0, 0)  # So csm polys won't show while drawing.

    # Instantiate moon turtle
    image_moon = 'moon_27x27.gif'
    screen.register_shape(image_moon)
    moon = Body(32000, (344, 42), Vec(-27, 147), gravsys, image_moon)
    moon.pencolor('gray')

    # Build command-service-module(csm)shape
    csm = Shape('compound')
    cm = ((0, 30), (0, -30), (30, 0))
    csm.addcomponent(cm, 'white', 'white')  # Silver and red are also good.
    sm = ((-60, 30), (0, 30), (0, -30), (-60, -30))
    csm.addcomponent(sm, 'white', 'black')    
    nozzle = ((-55, 0), (-90, 20), (-90, -20))
    csm.addcomponent(nozzle, 'white', 'white')
    screen.register_shape('csm', csm)

    # Instantiate Apollo 8 CSM turtle
    ship = Body(1, (Ro_X, Ro_Y), Vec(Vo_X, Vo_Y), gravsys, 'csm')
    ship.shapesize(0.2)
    ship.color('white')  # Path color. Silver and red are also good.
    ship.getscreen().tracer(1, 0)
    ship.setheading(90)

    gravsys.sim_loop()

if __name__ == '__main__':
    main()
