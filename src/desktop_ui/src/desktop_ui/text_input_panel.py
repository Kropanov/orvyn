from kivy.graphics import Color, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class TextInputPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(TextInputPanel, self).__init__(**kwargs)
        self.size_hint_x = None
        self.size_hint_y = None

        self.height = 50
        self.width = 650

        text_input = TextInput(multiline=True, hint_text="Enter text here...")
        text_input.cursor_color = (1, 1, 1, 1)
        text_input.foreground_color = (1, 1, 1, 1)
        text_input.background_color = (0.21, 0.21, 0.21, 1)
        text_input.background_normal = ""
        text_input.background_active = ""

        self.add_widget(text_input)

        with self.canvas.before:
            Color(0.21, 0.21, 0.21, 1)
            self.border_line = Line(
                points=[self.x, self.top, self.x + self.width, self.top], width=3
            )

        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border_line.points = [
            self.x,
            self.top,
            self.x + self.width,
            self.top,
            self.x + self.width,
            self.y,
            self.x,
            self.y,
            self.x,
            self.top,
        ]
