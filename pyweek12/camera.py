from __future__ import division
from math import sin, cos

from pyglet.gl import (
    glLoadIdentity, glMatrixMode,
    gluLookAt, gluOrtho2D,
    GL_MODELVIEW, GL_PROJECTION,
)


class Camera(object):
    """
    Camera tracks a position, orientation and zoom level, and applies openGL
    transforms so that subsequent renders are drawn at the correct place, size
    and orientation on screen
    """

    def __init__(self, offset, scale, angle=0.0):
        self.x, self.y = offset
        self.scale = scale
        self.angle = angle


    def world_projection(self, aspect):
        """
        Given aspect, ratio of screen width / height,
        Sets OpenGL projection and modelview matrices such that the window
        is centered on self.(x,y), shows at least scale world units in every
        direction, and is oriented by angle.
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if aspect >= 1:
            # landscape
            gluOrtho2D(
                -self.scale * aspect,
                +self.scale * aspect,
                -self.scale,
                +self.scale)
        else:
            # portrait
            gluOrtho2D(
                -self.scale,
                +self.scale,
                -self.scale / aspect,
                +self.scale / aspect)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self.x, self.y, +1.0,
            self.x, self.y, -1.0,
            sin(self.angle), cos(self.angle), 0.0)


    def hud_projection(self, size):
        """
        Sets OpenGL pojection and modelview matrices such that the window
        renders (0,0) to (size.x, size,y)
        """
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, size[0], 0, size[1])

