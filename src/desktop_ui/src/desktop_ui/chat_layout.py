from kivy.uix.boxlayout import BoxLayout

from desktop_ui.chat_body import ChatBody
from desktop_ui.chat_header import ChatHeader


class ChatLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatLayout, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.chat_header = ChatHeader()
        self.chat_body = ChatBody()

        self.add_widget(self.chat_header)
        self.add_widget(self.chat_body)

    def update_header_text(self, new_text):
        self.chat_header.label.text = new_text
