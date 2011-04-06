from __future__ import division
from math import sin, cos

from pyglet.gl import (
    glLoadIdentity, glMatrixMode, glViewport,
    gluLookAt, gluOrtho2D,
    GL_MODELVIEW, GL_PROJECTION,
)


class Camera(object):
    """
    Camera tracks a position, scale and angle, and applies openGL
    transforms so that subsequent renders are drawn at the correct place, size
    and orientation on screen
    """
    def __init__(self, offset, scale, angle=0.0):
        self.x, self.y = offset
        self.scale = scale
        self.angle = angle
        
        self.width = None
        self.height = None


    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        self.width = width
        self.height = height


    def world_projection(self):
        """
        Sets OpenGL projection and modelview matrices such that the window
        is centered on self.(x,y), shows at least 'scale' world units in every
        direction, and is oriented by angle.
        """
        left = bottom = -self.scale
        right = top = self.scale
        aspect = self.width / self.height
        if aspect >= 1:
            # landscape
            left *= aspect
            right *= aspect
        else:
            # portrait
            bottom /= aspect
            top /= aspect
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(left, right, bottom, top)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.x, self.y, +1.0,
            self.x, self.y, -1.0,
            sin(self.angle), cos(self.angle), 0.0)


    def hud_projection(self):
        """
        Sets OpenGL pojection and modelview matrices such that the window
        renders (0,0) to (size.x, size,y)
        """
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.width, 0, self.height)

