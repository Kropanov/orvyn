import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from desktop_ui.chat_layout import ChatLayout
from desktop_ui.sidebar import Sidebar

kivy.require("2.3.1")


class AppWindow(App):
    title = "Orvyn"

    def build(self):
        self.main_layout = BoxLayout()

        self.sidebar = Sidebar(app=self)
        self.chat_layout = ChatLayout()
        self.current_module = self.chat_layout

        self.main_layout.add_widget(self.sidebar)
        self.main_layout.add_widget(self.chat_layout)

        return self.main_layout

    def switch_module(self, module):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.sidebar)
        self.main_layout.add_widget(module)
        self.current_module = module


def main():
    AppWindow().run()


if __name__ == "__main__":
    main()
