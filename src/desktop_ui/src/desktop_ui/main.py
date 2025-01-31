import kivy
from kivy.app import App
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

kivy.require("2.3.1")


class FirstLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FirstLayout, self).__init__(**kwargs)

        self.size_hint_x = None
        self.width = 50

        with self.canvas.before:
            # Background color (black)
            Color(0, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class SecondLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super(SecondLayout, self).__init__(**kwargs)
        self.anchor_x = "center"
        self.anchor_y = "bottom"
        self.size_hint_x = 1
        self.size_hint_y = 1


class ThirdLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ThirdLayout, self).__init__(**kwargs)
        self.size_hint_x = None
        self.size_hint_y = None
        self.height = 50
        self.width = 650
        text_input = TextInput(multiline=True)
        text_input.background_color = (0, 0, 0, 1)
        text_input.foreground_color = (1, 1, 1, 1)
        text_input.hint_text = "Enter text here..."

        self.add_widget(text_input)
        # Add a white top border using canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.border_line = Line(
                points=[self.x, self.top, self.x + self.width, self.top], width=1
            )

        # Bind size and position updates
        self.bind(pos=self.update_border, size=self.update_border)

    def update_border(self, *args):
        self.border_line.points = [self.x, self.top, self.x + self.width, self.top]


class Application(App):
    title = "Orvyn"

    def build(self):
        main_layout = BoxLayout()
        main_layout.add_widget(FirstLayout())

        second_layout = SecondLayout()
        second_layout.add_widget(ThirdLayout())

        main_layout.add_widget(second_layout)

        return main_layout


def main():
    Application().run()


if __name__ == "__main__":
    main()
