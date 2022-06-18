import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

import constants
from rendering import getDeltaTime


class Point:
    radius = 5
    sides = 32

    def __init__(self, x, y, mass):
        """Initialise a point
        
        pos             Position vector of point
        velocity        Velocity vector of point
        mass            Mass (g) of point
        force           Force vector of point
        connections     Array of connections
        """
        self.position = np.array([float(x), float(y)])
        self.velocity = np.array([0.0, 0.0])
        self.mass = mass
        self.force = np.array([0.0, 0.0])
        self.connections = []
    
    def connect(self, other):
        self.connections.append(other)

    def draw(self):
        # draw a circle
        self.__draw_connections()
        self.__draw_point()
    
    def update(self):
        self.force = np.array([0.0, 0.0])

        # add forces
        # gravity
        self.force += np.array([0.0, -constants.GRAVITY * self.mass])

        # add to velocity
        self.velocity += (self.force * getDeltaTime()) / self.mass

        # modify position vector
        self.position += self.velocity * getDeltaTime()

        print(f"Force: {self.force}\nVelocity: {self.velocity}\nPosition: {self.position}\n\n")

    def __draw_point(self):
        glColor3f(255, 0, 0)
        glBegin(GL_POLYGON)
        
        for i in range(Point.sides):
            deg = 360 / Point.sides * i
            base = Point.radius * math.cos(math.radians(deg)) + self.position[0]
            height = Point.radius * math.sin(math.radians(deg)) + self.position[1]
            glVertex2f(base, height)
        
        glEnd()
    
    def __draw_connections(self):
        glColor3f(0, 255, 0)
        for connection in self.connections:
            glBegin(GL_LINES)
            glVertex2f(self.position[0], self.position[1])
            glVertex2f(connection.position[0], connection.position[1])
            glEnd()