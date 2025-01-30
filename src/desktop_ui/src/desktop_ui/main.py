import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle
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
            Color(0.2, 0.6, 0.8, 1)
            self.rect = Rectangle(pos=(0, 0), size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = self.size
        self.rect.pos = (0, 0)


class SecondLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(SecondLayout, self).__init__(**kwargs)
        self.size_hint_x = 1
        self.size_hint_y = 1

        with self.canvas.before:
            Color(0.33, 0.33, 0.33, 1)
            self.rect = Rectangle(pos=(0, 0), size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos


class ThirdLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super(ThirdLayout, self).__init__(**kwargs)
        self.size_hint_x = 1
        self.size_hint_y = None
        self.height = 50
        self.anchor_x = "left"
        self.anchor_y = "bottom"
        text_input = TextInput(multiline=True)
        text_input.background_color = (0.33, 0.33, 0.33, 1)
        self.add_widget(text_input)


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
