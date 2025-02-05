from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from desktop_ui.utils import get_img_path


class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_x = None
        self.padding = (0, 6, 0, 0)
        self.spacing = -5
        self.width = 50

        with self.canvas.before:
            Color(0.20, 0.20, 0.20, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        file_path = get_img_path("ollama.png")
        img = Image(source=file_path, size_hint_y=None, height=50)
        self.add_widget(img)

        file_path = get_img_path("deepseek.png")
        img = Image(source=file_path, size_hint_y=None, height=50)
        self.add_widget(img)

        file_path = get_img_path("openai.png")
        img = Image(source=file_path, size_hint_y=None, height=50)
        self.add_widget(img)

        file_path = get_img_path("claude.png")
        img = Image(source=file_path, size_hint_y=None, height=50)
        self.add_widget(img)

        file_path = get_img_path("gemini.png")
        img = Image(source=file_path, size_hint_y=None, height=50)
        self.add_widget(img)

        self.add_widget(Widget())

        file_path = get_img_path("module.png")
        img = Image(source=file_path, size_hint_y=None, height=50)
        self.add_widget(img)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
