
from pyglet import gl, clock
import rabbyt


class Render(object):

    def __init__(self, world, options):
        self.world = world
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
        self.clear_window(self.world.background_color)
        #self.projection.set_perspective(45)
        #self.modelview.set_world()
        self.draw_world()
        if self.options.fps:
            if self.clock_display is None:
                self.clock_display = clock.ClockDisplay()
            self.draw_hud()


    def draw_world(self):
        for item in self.world:
            item.render()


    def draw_hud(self):
        '''
        Draw any display items overlaid on the world, such as FPS counter
        '''
        #self.projection.set_screen()
        #self.modelview.set_identity()
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)

        self.clock_display.draw()

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisableClientState(gl.GL_COLOR_ARRAY)

