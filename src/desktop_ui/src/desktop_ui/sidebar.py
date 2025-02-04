from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout


class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)

        self.size_hint_x = None
        self.width = 50

        with self.canvas.before:
            Color(0.20, 0.20, 0.20, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
