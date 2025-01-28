import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("2.3.1")


class Application(App):
    def build(self):
        return Label(text="Hello world!")


def main():
    Application().run()


if __name__ == "__main__":
    main()
