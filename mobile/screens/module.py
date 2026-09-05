from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

from mobile.config import APP_NAME, PRIMARY, SECONDARY, SUCCESS, WHITE
from mobile.ui import font_name, rtl_text


class ModuleScreen(Screen):

    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)
        self.app_state = app_state
        self.module_key = ""
        self._build()

    def _build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=dp(14),
            spacing=dp(10),
        )

        self.title_label = Label(
            text=rtl_text(APP_NAME),
            font_name=font_name(),
            font_size="22sp",
            color=PRIMARY,
            size_hint_y=None,
            height=dp(56),
        )
        root.add_widget(self.title_label)

        scroll = ScrollView()

        self.body = BoxLayout(
            orientation="vertical",
            padding=dp(8),
            spacing=dp(10),
            size_hint_y=None,
        )

        self.body.bind(
            minimum_height=self.body.setter("height")
        )

        scroll.add_widget(self.body)
        root.add_widget(scroll)

        back = Button(
            text=rtl_text("بازگشت به داشبورد"),
            font_name=font_name(),
            background_normal="",
            background_color=PRIMARY,
            color=WHITE,
            size_hint_y=None,
            height=dp(52),
        )

        back.bind(on_release=self.go_back)

        root.add_widget(back)
        self.add_widget(root)

    def show_module(self, title, key, role=None):

        self.module_key = key or ""

        self.title_label.text = rtl_text(
            title or APP_NAME
        )

        self.body.clear_widgets()

        role_text = role or "کاربر"

        self.body.add_widget(
            Label(
                text=rtl_text(
                    f"{title}\n\nنقش: {role_text}"
                ),
                font_name=font_name(),
                font_size="18sp",
                color=PRIMARY,
                size_hint_y=None,
                height=dp(100),
            )
        )

        self.body.add_widget(
            Label(
                text=rtl_text(
                    "این بخش در نسخه موبایل فراهوش فعال است."
                ),
                font_name=font_name(),
                font_size="15sp",
                color=SECONDARY,
                halign="center",
                valign="middle",
                size_hint_y=None,
                height=dp(100),
            )
        )

        refresh = Button(
            text=rtl_text("بازخوانی"),
            font_name=font_name(),
            background_normal="",
            background_color=SUCCESS,
            color=WHITE,
            size_hint_y=None,
            height=dp(50),
        )

        refresh.bind(
            on_release=lambda *_:
            self.show_module(title, key, role)
        )

        self.body.add_widget(refresh)

    def go_back(self, *_):

        if (
            self.manager
            and self.manager.has_screen("dashboard")
        ):
            self.manager.current = "dashboard"                      
