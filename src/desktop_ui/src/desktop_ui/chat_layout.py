from kivy.uix.anchorlayout import AnchorLayout


class ChatLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super(ChatLayout, self).__init__(**kwargs)
        self.anchor_x = "center"
        self.anchor_y = "bottom"
        self.size_hint_x = 1
        self.size_hint_y = 1
