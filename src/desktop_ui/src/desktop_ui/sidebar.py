from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from desktop_ui.icon_button import IconButton
from desktop_ui.utils import get_img_path


class SidebarModule:
    def __init__(self, module_name, icon, is_top_section=True):
        self.module_name = module_name
        self.icon = icon
        self.is_top_section = is_top_section


class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)

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
            SidebarModule("ollama", "ollama.png"),
            SidebarModule("deepseek", "deepseek.png"),
            SidebarModule("openai", "openai.png"),
            SidebarModule("claude", "claude.png"),
            SidebarModule("gemini", "gemini.png"),
            SidebarModule("settings", "module.png", is_top_section=False),
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

    def _add_sidebar_button(self, module: SidebarModule):
        """Create sidebar button and add it to the sidebar"""
        file_path = get_img_path(module.icon)
        button = IconButton(
            source=file_path,
            module_name=module.module_name,
            size_hint_y=None,
            height=50,
        )
        self.add_widget(button)
