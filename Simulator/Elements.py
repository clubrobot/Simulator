from Physics_tools import *
from Server_utils.Wheeledbase_virtual import *
from Server_utils.Buildingcollector_virtual import *
from Server_utils.Waterdispenser_virtual import *
from Server_utils.display_virtual import *
from Server_utils.sensors_virtual import *
import math


class Dispenser():
    def __init__(self, parent, x, y, radius, color, capacity=8, min_ang=-0.785398, max_ang=0.785398):
        self.x = x
        self.y = y
        self.min_ang = min_ang
        self.max_ang = max_ang
        self.parent = parent
        self.parent.add_dispenser(self)
        self.radius = radius
        self.container = list()
        self.linked_ball = list()
        if(type(color) == list):
            color_list = list(color)*(capacity//len(color))
        else:
            color_list = [color]*capacity
        for col in color_list:
            self.linked_ball.append(Ball(self.parent, col))
        for ball in self.linked_ball:
            self.container.append(ball)

    def reset(self):
        self.container = list()
        for ball in self.linked_ball:
            ball.reset()
            self.container.append(ball)

    def getball(self, x, y, theta):
        if(math.hypot(y-self.y, x-self.x) < self.radius):

            # and theta>self.min_ang and theta<self.max_ang):
            if(len(self.container) > 0):
                return self.container.pop()
        return None


class Cup(Object):
    number = 0
    radius = 36

    def __init__(self, parent, color="green", x=1000, y=1000, theta=0):
        self.name = "Cup_{}".format(Cup.number)
        Cup.number += 1
        Object.__init__(self, self.name, parent, x, y, theta)
        self.polygone = ((-Cup.radius, -Cup.radius),
                         (Cup.radius, -Cup.radius),
                         (Cup.radius, Cup.radius),
                         (-Cup.radius, Cup.radius))
        self.parent.core.setShape(self.name, self.polygone)
        self.parent.core.setWeight(self.name, 5)
        self.initial_coordinates = (x, y)
        self.shape = self.canvas.create_oval(
            *self.canvas.convert_polygon((self.polygone[0], self.polygone[2])), fill=color)
        self.canvas.itemconfig(self.shape, fill=color)
        self.scored = None
        self.points = 5

    def reset(self):
        self.parent.core.setPosition(self.name, *self.initial_coordinates)
        self.parent.core.enableObject(self.name)
        self.scored = None

    def forward(self):
        self.parent.core.setVelocity(self.name, 100, 0, False)

    def refresh(self):
        poly = self.canvas.convert_polygon(
            self.parent.core.getShape(self.name))
        self.canvas.coords(self.shape, poly[0], poly[1], poly[4], poly[5])


class Robot(Object):
    def __init__(self, name, parent, color, x=1000, y=1000, theta=0, container_size=6):
        Object.__init__(self, name, parent, x, y, theta)
        self.polygone = ((-57.5, -93.5), (-57.5, 93.5), (-38.5, 112.5), (38.5, 112.5),
                         (57.5, 93.5), (57.5, -93.5), (38.5, -112.5), (-38.5, -112.5))
        #self.polygone  =(  (-93.5,57.5) , (93.5,57.5),(112.5,38.5) ,(112.5,-38.5),(93.5,-57.5),(-93.5,-57.5),(-112.5,-38.5),(-112.5,38.5))
        #self.polygone = ( (-100,40),(100,40),(100,-40),(-100,-40)  )
        self.parent.core.setShape(self.name, self.polygone)
        self.shape = self.canvas.create_polygon(self.polygone)
        self.color = color
        self.parent.core.setWeight(self.name, 3000)
        self.arduinos = [Wheeledbase(self), Display(self), Sensors(self)]
        self.parent.core.setMaxAcceleration(self.name, 200, 2)
        self.parent.core.setMinAcceleration(self.name, 200, 2)

        self.container = list()
        self.container_size = container_size

        self.x = 0
        self.y = 0
        self.theta = 0
        self.polygone = tuple()

    def clear(self):
        print("suppression")
        self.canvas.delete(self.shape)
        time.sleep(0.1)
        self.canvas.remove_components(self)
        self.parent.remove(self)

    def compute(self):
        self.x, self.y = self.parent.core.getPosition(self.name)
        self.theta = self.parent.core.getTheta(self.name)
        self.polygone = self.parent.core.getShape(self.name)
        if(hasattr(self, 'arduinos')):
            for arduino in self.arduinos:
                arduino.compute()

    def refresh(self):
        self.canvas.coords(
            self.shape, *(self.canvas.convert_polygon(self.parent.core.getShape(self.name))))

    def pick_cup(self, id):
        for x, y in self.polygone:
            cup_taken = self.parent.core.getObject(x, y, 50)
            if not cup_taken in ["None", self.name]:
                self.parent.core.setPosition(cup_taken, -100, -100)
                self.container.append(cup_taken)
                break

    def put_cup(self, id):
        pass
