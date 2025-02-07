from kivy.uix.boxlayout import BoxLayout

from desktop_ui.chat_body import ChatBody
from desktop_ui.chat_header import ChatHeader


class ChatLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatLayout, self).__init__(**kwargs)
        self.orientation = "vertical"

        chat_header = ChatHeader()
        chat_body = ChatBody()

        self.add_widget(chat_header)
        self.add_widget(chat_body)
