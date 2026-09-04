from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

from mobile.config import (
    APP_NAME,
    PRIMARY,
    SECONDARY,
    SUCCESS,
    WHITE,
)

from mobile.ui import font_name, rtl_text


ROLE_LABELS = {
    "manager": "مدیریت",
    "admin": "مدیریت",
    "teacher": "دبیر",
    "student": "دانش‌آموز",
    "parent": "ولی",
}


ROLE_MODULES = {

    "manager": [
        "مدیریت مدرسه",
        "کلاس‌ها",
        "امتحانات",
        "گزارش‌ها",
        "پیام‌ها",
    ],

    "teacher": [
        "کلاس‌های من",
        "حضور و غیاب",
        "نمرات",
        "آزمون‌ها",
    ],

    "student": [
        "کلاس من",
        "برنامه هفتگی",
        "امتحانات",
        "نمرات",
    ],

    "parent": [
        "فرزندان من",
        "نمرات",
        "پرداخت‌ها",
    ],

}


class DashboardScreen(Screen):

    def __init__(self, app_state, **kwargs):

        super().__init__(**kwargs)

        self.app_state = app_state


        root = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(10)
        )


        self.header = Label(
            font_name=font_name(),
            font_size="20sp",
            color=PRIMARY,
            size_hint_y=None,
            height=dp(80)
        )


        root.add_widget(
            self.header
        )


        scroll = ScrollView()


        self.grid = GridLayout(
            cols=2,
            spacing=dp(10),
            size_hint_y=None
        )


        self.grid.bind(
            minimum_height=self.grid.setter("height")
        )


        scroll.add_widget(
            self.grid
        )


        root.add_widget(scroll)


        self.add_widget(root)


        self.refresh()



    def refresh(self):

        self.grid.clear_widgets()


        if self.app_state is None:

            self.header.text = rtl_text(
                "فراهوش\nدر حال آماده‌سازی..."
            )

            return



        try:

            role = self.app_state.role

            name = self.app_state.display_name


        except Exception:

            role = "student"
            name = "کاربر فراهوش"



        label = ROLE_LABELS.get(
            role,
            "کاربر"
        )


        self.header.text = rtl_text(
            f"{APP_NAME}\n{name} - {label}"
        )


        modules = ROLE_MODULES.get(
            role,
            ROLE_MODULES["student"]
        )


        for module in modules:

            btn = Button(
                text=rtl_text(module),
                font_name=font_name(),
                background_normal="",
                background_color=SECONDARY,
                color=WHITE
            )


            btn.bind(
                on_release=lambda x, m=module:
                self.open_module(m)
            )


            self.grid.add_widget(btn)



        update = Button(
            text=rtl_text("مرکز به‌روزرسانی"),
            font_name=font_name(),
            background_normal="",
            background_color=SUCCESS,
            color=WHITE
        )


        update.bind(
            on_release=self.open_update
        )


        self.grid.add_widget(update)



        logout = Button(
            text=rtl_text("خروج"),
            font_name=font_name(),
            background_normal="",
            background_color=PRIMARY,
            color=WHITE
        )


        logout.bind(
            on_release=self.logout
        )


        self.grid.add_widget(logout)



    def open_module(self, name):

        screen = self.manager.get_screen(
            "module"
        )

        screen.show_module(
            name,
            self.app_state.role
        )

        self.manager.current = "module"



    def open_update(self, *_):

        self.manager.current = "update"



    def logout(self, *_):

        if self.app_state:

            self.app_state.logout()


        self.manager.current = "login"       
