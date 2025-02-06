from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


# OPTIMIZE: instances and on_mouse_move
class IconButton(ButtonBehavior, Image):
    instances = []
    _mouse_bound = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        IconButton.instances.append(self)

        if not IconButton._mouse_bound:
            Window.bind(mouse_pos=IconButton.on_mouse_move)
            IconButton._mouse_bound = True

    def on_press(self):
        Logger.info(f"IconButton: Pressed {self.source}")

    def on_release(self):
        Logger.info(f"IconButton: Out {self.source}")

    @classmethod
    def on_mouse_move(cls, window, pos):
        hovered_any = False

        for instance in cls.instances:
            if not instance.get_root_window():
                continue

            widget_pos = instance.to_widget(*pos)
            if instance.collide_point(*widget_pos):
                hovered_any = True
                break

        # current_cursor = (
        #     window.system_cursor if hasattr(window, "system_cursor") else None
        # )
        if hovered_any:
            Window.set_system_cursor("hand")
        else:
            Window.set_system_cursor("arrow")
