from pyglet import font
from pyglet.gl import glColor4f
import rabbyt

from .gameitem import GameItem

font.add_directory('pyweek12/data')
default_font = font.load('Computerfont', 48)

class SpriteText(rabbyt.BaseSprite):
    def __init__(self, text, fnt=default_font, color=(1, 0.54, 0, 1), **kwargs):
        rabbyt.BaseSprite.__init__(self, **kwargs)
        self.fnt = fnt
        self.color = color
        self.set_text(text)

    def set_text(self, text):
        self.text = text
        glyphs = self.fnt.get_glyphs(text)
        self.glyph_string = font.GlyphString(text, glyphs)

    def render_after_transform(self):
        glColor4f(*self.color)
        self.glyph_string.draw()


class LivesMessage(GameItem):

    layer = 4

    def __init__(self, lives):
        self.sprite = SpriteText('', xy=(50,50))
        GameItem.__init__(self)
        self.update_lives(lives)
        
    def update_lives(self, lives):
        self.sprite.set_text('Tanks: %s' % (lives,))


class TimeMessage(GameItem):

    layer = 4

    def __init__(self, time, window_width):
        self.sprite = SpriteText('', xy=(300,50))
        self.time = time
        self.window_width = window_width
        GameItem.__init__(self)
        
    def set_time(self, time):
        self.time = time

    def update(self, age, dt):
        self.time -= dt
        self.sprite.set_text('%1.1f' % (max(self.time, 0),))
        self.sprite.x = (self.window_width - 200 + (
                60 - self.sprite.glyph_string.get_subwidth(0, 1)))
    

class MainMenu(GameItem):
    pass

