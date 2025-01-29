import kivy
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout

kivy.require("2.3.1")


class FirstLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FirstLayout, self).__init__(**kwargs)

        self.size_hint = (0.06, 1)

        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)
            self.rect = Rectangle(pos=(0, 0), size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        # Update the rectangle size and position when the layout changes
        self.rect.size = self.size
        self.rect.pos = (0, 0)


class SecondLayout(ScatterLayout):
    def __init__(self, **kwargs):
        super(SecondLayout, self).__init__(**kwargs)
        self.size_hint = (0.94, 1)
        self.cols = 2

        with self.canvas.before:
            Color(0.1, 0.2, 0.1, 1)
            self.rect = Rectangle(pos=(0, 0), size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(Label(text="Hello world!"))

    def _update_rect(self, instance, value):
        # Update the rectangle size and position when the layout changes
        self.rect.size = instance.size
        self.rect.pos = (0, 0)


class Application(App):
    title = "Orvyn"

    def build(self):
        main_layout = BoxLayout()
        main_layout.add_widget(FirstLayout())
        main_layout.add_widget(SecondLayout())

        return main_layout


def main():
    Application().run()


if __name__ == "__main__":
    main()
