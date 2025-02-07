from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout


class ChatHeader(StackLayout):
    def __init__(
        self,
        label="deepseek",
        **kwargs,
    ):
        super(ChatHeader, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 50

        with self.canvas.before:
            Color(0.31, 0.31, 0.31, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        self.label = Label(text=label, bold=True, color=(1, 1, 1, 1))
        self.add_widget(self.label)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
