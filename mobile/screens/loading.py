from kivy.clock import Clock
from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.metrics import dp

from mobile.config import APP_NAME, SYSTEM_TITLE, LOGO_PATH, PRIMARY, SECONDARY, BACKGROUND
from mobile.ui import font_name, rtl_text


class LoadingScreen(Screen):
    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)
        self.app_state = app_state
        self.add_widget(self._build())
        Clock.schedule_once(self._finish, 0.65)

    def _build(self):
        root = BoxLayout(orientation="vertical", padding=dp(28), spacing=dp(12))
        root.add_widget(BoxLayout(size_hint_y=0.22))
        from pathlib import Path
        if Path(LOGO_PATH).exists():
            root.add_widget(Image(source=LOGO_PATH, size_hint_y=None, height=dp(150), allow_stretch=True, keep_ratio=True))
        title = Label(text=rtl_text(APP_NAME), font_name=font_name(), font_size="34sp", bold=True, color=PRIMARY, size_hint_y=None, height=dp(60))
        subtitle = Label(text=rtl_text(SYSTEM_TITLE), font_name=font_name(), font_size="16sp", color=SECONDARY, size_hint_y=None, height=dp(45))
        root.add_widget(title)
        root.add_widget(subtitle)
        root.add_widget(Label(text=rtl_text("در حال آماده‌سازی برنامه..."), font_name=font_name(), font_size="13sp", color=SECONDARY, size_hint_y=None, height=dp(36)))
        root.add_widget(BoxLayout(size_hint_y=0.45))
        return root

    def _finish(self, *_):
        if not self.manager:
            return
        self.manager.current = "dashboard" if self.app_state.logged_in else "login"
