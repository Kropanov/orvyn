from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout

from desktop_ui.text_input_panel import TextInputPanel


class ChatBody(AnchorLayout):
    def __init__(self, **kwargs):
        super(ChatBody, self).__init__(**kwargs)
        self.anchor_x = "center"
        self.anchor_y = "bottom"

        self.size_hint_x = 1
        self.size_hint_y = 1

        with self.canvas.before:
            Color(0.31, 0.31, 0.31, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        text_input_panel = TextInputPanel()
        self.add_widget(text_input_panel)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
