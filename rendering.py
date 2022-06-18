import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

oldTimeSinceStart = 0

def getDeltaTime():
    global oldTimeSinceStart

    timeSinceStart = glutGet(GLUT_ELAPSED_TIME)
    deltaTime = timeSinceStart - oldTimeSinceStart
    oldTimeSinceStart = timeSinceStart

    return deltaTime