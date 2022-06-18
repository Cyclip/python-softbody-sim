import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from elements import Point

objects = []
width, height = 800, 700

def genPoints():
    global objects
    """
       A       B
        •-----•
        |     |
        |     |
        •-----•
       D       C
    """
    a = Point(400, 500, 2)
    b = Point(500, 500, 2)
    c = Point(500, 400, 2)
    d = Point(400, 400, 2)

    #a.connect(b)
    #b.connect(c)
    #c.connect(d)
    #d.connect(a)
    #d.connect(b)
    #a.connect(c)

    objects += [a,]#, b, c, d]
    

def refresh2d(width, height):
    """Tell OpenGL it is a 2D surface"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def main():
    genPoints()

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height) 
    glutInitWindowPosition(0, 0)
    
    glutCreateWindow("Empty Window")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glColor3f(0, 0, 0)
    glutMainLoop()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    refresh2d(width, height)

    for obj in objects:
        obj.draw()
        obj.update()

    glFlush()


if __name__ == "__main__":
    main()