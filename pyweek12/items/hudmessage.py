from pyglet import font
import rabbyt

from .gameitem import GameItem

font.add_directory('pyweek12/data')
default_font = font.load('Computerfont', 24)

class SpriteText(rabbyt.BaseSprite):
    def __init__(self, text, fnt=default_font, **kwargs):
        rabbyt.BaseSprite.__init__(self, **kwargs)
        self._text = font.Text(fnt, text)

    def set_text(self, text):
        self._text.text = text

    def render_after_transform(self):
        self._text.color = self.rgba
        self._text.draw()


class HudMessage(GameItem):

    layer = 4

    def __init__(self, text, *args, **kwargs):
        self.sprite = SpriteText(text, *args, **kwargs)
        GameItem.__init__(self, *args, **kwargs)


class MainMenu(GameItem):
    pass

