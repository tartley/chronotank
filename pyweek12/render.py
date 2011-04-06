
from __future__ import division
from pyglet import gl, clock
import rabbyt


class Render(object):

    def __init__(self, world, camera, options):
        self.world = world
        self.camera = camera
        self.options = options
        self.clock_display = None
        rabbyt.set_default_attribs()

    def clear_window(self, color):
        '''
        Clear window color and depth buffers, using the given color
        '''
        r, g, b, _ = color
        gl.glClearColor(r, g, b, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)


    def draw(self):
        '''
        Redraw the whole window
        '''
        self.camera.update(self.camera)
        self.clear_window(self.world.background_color)
        self.camera.world_projection()
        for item in self.world:
            item.sprite.render()

        self.draw_hud()



    def draw_hud(self):
        '''
        Draw any display items overlaid on the world, such as FPS counter
        '''
        self.camera.hud_projection()
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)

        if self.options.fps:
            if self.clock_display is None:
                self.clock_display = clock.ClockDisplay()
            self.clock_display.draw()

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisableClientState(gl.GL_COLOR_ARRAY)

