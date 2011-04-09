from pyglet import font
import rabbyt

from .gameitem import GameItem

font.add_directory('pyweek12/data')
default_font = font.load('Computerfont', 48)

class SpriteText(rabbyt.BaseSprite):
    def __init__(self, text, fnt=default_font, **kwargs):
        rabbyt.BaseSprite.__init__(self, **kwargs)
        self._text = font.Text(fnt, text)

    def set_text(self, text):
        self._text.text = text

    def render_after_transform(self):
        self._text.color = self.rgba
        self._text.draw()


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
        if time < 0:
            self.time = 0
        else:
            self.time = time

    def update(self, dt):
        self.time -= dt
        self.sprite.set_text('%.1f' % (self.time,))
        self.sprite.x = self.window_width - 50 - self.sprite._text.width
    

class MainMenu(GameItem):
    pass

