import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from desktop_ui.chat_layout import ChatLayout
from desktop_ui.sidebar import Sidebar

kivy.require("2.3.1")


class AppWindow(App):
    title = "Orvyn"

    def build(self):
        main_layout = BoxLayout()

        sidebar = Sidebar()
        chat_layout = ChatLayout()

        main_layout.add_widget(sidebar)
        main_layout.add_widget(chat_layout)

        return main_layout


def main():
    AppWindow().run()


if __name__ == "__main__":
    main()
