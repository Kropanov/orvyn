from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

# from desktop_ui.chat_header import ChatHeader


class IconButton(ButtonBehavior, Image):
    instances = []
    _mouse_bound = False
    # chat_header = ChatHeader()

    def __init__(self, on_press_run, module_name="", **kwargs):
        super().__init__(**kwargs)
        IconButton.instances.append(self)
        self.hovered = False
        self.hover_box = None
        self.module_name = module_name
        self.on_press_run = on_press_run

        if not IconButton._mouse_bound:
            Window.bind(mouse_pos=IconButton.on_mouse_move)
            IconButton._mouse_bound = True

    def on_press(self):
        Logger.info(f"IconButton: {self.module_name} module is loaded")
        self.on_press_run()

    def on_release(self):
        pass

    def show_hover_box(self):
        if self.hover_box is None:
            with self.canvas.after:
                self.hover_color = Color(1, 1, 1, 0.3)
                self.hover_box = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_hover_box, size=self.update_hover_box)
        self.hovered = True

    def update_hover_box(self, *args):
        if self.hover_box:
            self.hover_box.pos = self.pos
            self.hover_box.size = self.size

    def hide_hover_box(self):
        if self.hover_box:
            self.canvas.after.remove(self.hover_color)
            self.canvas.after.remove(self.hover_box)
            self.hover_box = None
            self.unbind(pos=self.update_hover_box, size=self.update_hover_box)
        self.hovered = False

    @classmethod
    def on_mouse_move(cls, window, pos):
        hovered_any = False

        for instance in cls.instances:
            if not instance.get_root_window():
                continue

            widget_pos = instance.to_widget(*pos)
            if instance.collide_point(*widget_pos):
                hovered_any = True
                if not instance.hovered:
                    instance.show_hover_box()
            else:
                if instance.hovered:
                    instance.hide_hover_box()

        if hovered_any:
            Window.set_system_cursor("hand")
        else:
            Window.set_system_cursor("arrow")
