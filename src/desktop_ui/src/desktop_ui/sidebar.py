from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from desktop_ui.chat_layout import ChatLayout
from desktop_ui.icon_button import IconButton
from desktop_ui.utils import get_img_path


class SidebarModule:
    def __init__(self, module_name, icon, is_top_section=True, module_cls=ChatLayout):
        self.icon = icon
        self.module_cls = module_cls
        self.module_name = module_name
        self.is_top_section = is_top_section


class Sidebar(BoxLayout):
    def __init__(self, app, **kwargs):
        super(Sidebar, self).__init__(**kwargs)

        self.app = app

        self.orientation = "vertical"
        self.size_hint_x = None
        self.padding = (0, 0, 0, 0)
        self.spacing = 0
        self.width = 50

        with self.canvas.before:
            Color(0.20, 0.20, 0.20, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.sidebar_modules = [
            SidebarModule("ollama", "ollama.png", module_cls=ChatLayout),
            SidebarModule("deepseek", "deepseek.png", module_cls=ChatLayout),
            SidebarModule("openai", "openai.png", module_cls=ChatLayout),
            SidebarModule("claude", "claude.png", module_cls=ChatLayout),
            SidebarModule("gemini", "gemini.png", module_cls=ChatLayout),
            SidebarModule(
                "settings", "module.png", is_top_section=False, module_cls=Widget
            ),
        ]

        top_modules = [mod for mod in self.sidebar_modules if mod.is_top_section]
        bottom_modules = [mod for mod in self.sidebar_modules if not mod.is_top_section]

        for module in top_modules:
            self._add_sidebar_button(module)

        if bottom_modules:
            self.add_widget(Widget())

        for module in bottom_modules:
            self._add_sidebar_button(module)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def _add_sidebar_button(self, sm: SidebarModule):
        """Create sidebar button and add it to the sidebar"""
        file_path = get_img_path(sm.icon)
        button = IconButton(
            source=file_path,
            module_name=sm.module_name,
            size_hint_y=None,
            height=50,
            on_press_run=lambda: self.switch_to_module(sm),
        )
        self.add_widget(button)

    def switch_to_module(self, sm: SidebarModule):
        new_module = sm.module_cls()
        current_module = self.app.current_module

        if isinstance(current_module, ChatLayout) and isinstance(
            new_module, ChatLayout
        ):
            Logger.info(f"module: updating header text to '{sm.module_name}'")
            current_module.update_header_text(sm.module_name)
            return

        Logger.info(f"module: switching to {sm.module_name}")
        self.app.switch_module(new_module)
