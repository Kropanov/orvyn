from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

from desktop_ui.metaclasses.singleton import Singleton

BaseMeta = type(StackLayout)


class CombinedSingleton(Singleton, BaseMeta):
    pass


class ChatHeader(StackLayout, metaclass=CombinedSingleton):
    def __init__(
        self,
        label_text="",
        **kwargs,
    ):
        super(ChatHeader, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 50

        with self.canvas.before:
            Color(0.31, 0.31, 0.31, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        self.label = Label(text=label_text, bold=True, color=(1, 1, 1, 1))
        self.add_widget(self.label)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def set_label_text(self, text):
        self.label.text = text
