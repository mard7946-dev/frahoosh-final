from kivy.animation import Animation

from kivy.graphics import (
    Color,
    RoundedRectangle,
    Rectangle,
    Line,
)

from kivy.metrics import dp
from kivy.properties import NumericProperty

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout


from mobile.config import (
    APP_NAME,
    SCHOOL_NAME,
    BACKGROUND_PATH,
)

from mobile.ui import (
    font_name,
    rtl_text,
)


ROLE_ALIASES = {

    "admin": "manager",
    "administrator": "manager",
    "manager": "manager",
    "مدیر": "manager",
    "مدیریت": "manager",

    "executive": "executive",
    "معاون اجرایی": "executive",

    "educational": "educational",
    "معاون آموزشی": "educational",

    "cultural": "cultural",
    "پرورشی": "cultural",
    "معاون پرورشی": "cultural",

    "advisor": "advisor",
    "مشاور": "advisor",

    "teacher": "teacher",
    "دبیر": "teacher",
    "معلم": "teacher",

    "student": "student",
    "دانش‌آموز": "student",
    "دانش آموز": "student",

    "parent": "parent",
    "ولی": "parent",
    "اولیا": "parent",
}


ROLE_TITLES = {

    "manager": "مدیریت",

    "executive": "معاون اجرایی",

    "educational": "معاون آموزشی",

    "cultural": "معاون پرورشی",

    "advisor": "مشاور",

    "teacher": "دبیر",

    "student": "دانش‌آموز",

    "parent": "ولی",
}



MANAGER_MENU = [

    ("مدیریت", "management"),
    ("معاون آموزشی", "educational"),
    ("معاون اجرایی", "executive"),
    ("معاون پرورشی", "cultural"),
    ("مشاوره", "advisor"),

    ("دبیران", "teachers"),
    ("اولیا", "parents"),
    ("دانش‌آموزان", "students"),

    ("مالی", "finance"),
    ("پرداخت آنلاین", "payment"),

    ("کلاس‌های آنلاین", "online"),

    ("تابلو هوشمند", "smart_board"),

    ("هوش مصنوعی", "ai"),

    ("گزارش‌ها", "reports"),

    ("پیام‌ها", "messages"),

    ("تنظیمات", "settings"),

]



ROLE_MENU = {


    "executive": [

        ("معاون اجرایی", "executive"),
        ("دانش‌آموزان", "students"),
        ("اولیا", "parents"),
        ("پیام‌ها", "messages"),
        ("تنظیمات", "settings"),

    ],


    "educational": [

        ("معاون آموزشی", "educational"),
        ("دانش‌آموزان", "students"),
        ("دبیران", "teachers"),
        ("کلاس آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("گزارش‌ها", "reports"),
        ("پیام‌ها", "messages"),

    ],


    "cultural": [

        ("معاون پرورشی", "cultural"),
        ("دانش‌آموزان", "students"),
        ("تابلو هوشمند", "smart_board"),
        ("پیام‌ها", "messages"),

    ],


    "advisor": [

        ("مشاوره", "advisor"),
        ("دانش‌آموزان", "students"),
        ("اولیا", "parents"),
        ("پیام‌ها", "messages"),

    ],


    "teacher": [

        ("پنل دبیر", "teacher"),
        ("دانش‌آموزان", "students"),
        ("کلاس آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("پیام‌ها", "messages"),

    ],


    "student": [

        ("پنل دانش‌آموز", "student"),
        ("برنامه هفتگی", "schedule"),
        ("وضعیت تحصیلی", "student_info"),
        ("پرداخت آنلاین", "payment"),
        ("کلاس آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("پیام‌ها", "messages"),

    ],


    "parent": [

        ("پنل اولیا", "parent"),
        ("وضعیت تحصیلی فرزند", "student_info"),
        ("پرداخت آنلاین", "payment"),
        ("کلاس آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("پیام‌ها", "messages"),

    ],

}



class HamburgerButton(Widget):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas:

            self.line_color = Color(
                1,
                1,
                1,
                1
            )

            self.line1 = Line(width=2)
            self.line2 = Line(width=2)
            self.line3 = Line(width=2)


        self.bind(
            pos=self._update,
            size=self._update
        )


    def _update(self, *_):

        left = self.x + self.width * 0.2
        right = self.x + self.width * 0.8


        self.line1.points = [
            left,
            self.center_y + dp(8),
            right,
            self.center_y + dp(8),
        ]


        self.line2.points = [
            left,
            self.center_y,
            right,
            self.center_y,
        ]


        self.line3.points = [
            left,
            self.center_y - dp(8),
            right,
            self.center_y - dp(8),
        ]



class DashboardScreen(Screen):


    drawer_width = NumericProperty(
        dp(320)
    )


    def __init__(self, app_state, **kwargs):

        super().__init__(**kwargs)

        self.app_state = app_state
        self.drawer_open = False

        self._build_ui()

    def _build_drawer(self):

        self.drawer.clear_widgets()


        title = Label(
            text=rtl_text(APP_NAME),
            font_name=font_name(),
            font_size="26sp",
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, None),
            height=dp(60),
            pos_hint={
                "top": 0.98
            }
        )

        self.drawer.add_widget(
            title
        )


        self.menu_role = Label(
            text="",
            font_name=font_name(),
            font_size="13sp",
            color=(
                0.7,
                0.9,
                1,
                1
            ),
            size_hint=(1, None),
            height=dp(40),
            pos_hint={
                "top": 0.88
            }
        )

        self.drawer.add_widget(
            self.menu_role
        )


        self.menu_scroll = ScrollView(
            size_hint=(0.95, 0.68),
            pos_hint={
                "center_x": 0.5,
                "top": 0.78
            },
            do_scroll_x=False
        )


        self.menu_box = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=dp(5),
            size_hint_y=None
        )


        self.menu_box.bind(
            minimum_height=
            self.menu_box.setter(
                "height"
            )
        )


        self.menu_scroll.add_widget(
            self.menu_box
        )


        self.drawer.add_widget(
            self.menu_scroll
        )


        self.logout_button = Button(
            text=rtl_text(
                "خروج از حساب"
            ),
            font_name=font_name(),
            background_normal="",
            background_color=(
                0.65,
                0.08,
                0.12,
                1
            ),
            color=(1, 1, 1, 1),
            size_hint=(0.88, None),
            height=dp(50),
            pos_hint={
                "center_x": 0.5,
                "y": 0.03
            }
        )


        self.logout_button.bind(
            on_release=self.logout
        )


        self.drawer.add_widget(
            self.logout_button
        )


    # -----------------------------------------
    # REFRESH
    # -----------------------------------------

    def refresh(self):

        role = self._get_role()

        name = self._get_display_name()


        title = ROLE_TITLES.get(
            role,
            "کاربر"
        )


        self.welcome_title.text = rtl_text(
            f"خوش آمدید، {name}"
        )


        self.role_label.text = rtl_text(
            f"نقش کاربری: {title}"
        )


        self.menu_role.text = rtl_text(
            f"{name} | {title}"
        )


        self._populate_menu(
            role
        )


    # -----------------------------------------
    # MENU
    # -----------------------------------------

    def _populate_menu(
        self,
        role
    ):

        self.menu_box.clear_widgets()


        items = (

            MANAGER_MENU

            if role == "manager"

            else ROLE_MENU.get(
                role,
                []
            )

        )


        for title, route in items:


            btn = Button(

                text=rtl_text(title),

                font_name=font_name(),

                font_size="14sp",

                background_normal="",

                background_color=(

                    0.05,

                    0.22,

                    0.34,

                    1

                ),

                color=(1, 1, 1, 1),

                size_hint_y=None,

                height=dp(46)

            )


            btn.bind(

                on_release=lambda x, r=route:
                self._menu_selected(r)

            )


            self.menu_box.add_widget(
                btn
            )


    # -----------------------------------------
    # NAVIGATION
    # -----------------------------------------

    def _menu_selected(
        self,
        route
    ):

        self.close_drawer()


        if not self.manager:
            return


        if not self.manager.has_screen(
            "module"
        ):
            return


        module = self.manager.get_screen(
            "module"
        )


        try:

            module.set_module(
                route
            )

            self.manager.current = (
                "module"
            )


        except Exception as exc:

            print(
                "MODULE ROUTE ERROR:",
                repr(exc)
            )


    # -----------------------------------------
    # ROLE
    # -----------------------------------------

    def _get_role(self):

        try:

            role = self.app_state.role

        except Exception:

            role = "student"


        role = str(
            role or "student"
        ).strip().lower()


        return ROLE_ALIASES.get(
            role,
            role
        )


    def _get_display_name(self):

        try:

            return (
                self.app_state.display_name
                or "کاربر فراهوش"
            )

        except Exception:

            return "کاربر فراهوش"

    # -----------------------------------------
    # DRAWER CONTROL
    # -----------------------------------------

    def _hamburger_touch(
        self,
        instance,
        touch
    ):

        if self.menu_button.collide_point(
            *touch.pos
        ):

            self.toggle_drawer()

            return True

        return False



    def toggle_drawer(self):

        if self.drawer_open:

            self.close_drawer()

        else:

            self.open_drawer()



    def open_drawer(self):

        if self.drawer_open:
            return


        self.drawer_open = True


        self.drawer_overlay.opacity = 1

        self.drawer_overlay.disabled = False


        Animation(
            x=0,
            duration=0.25
        ).start(
            self.drawer
        )



    def close_drawer(
        self,
        *_ 
    ):

        if not self.drawer_open:
            return


        self.drawer_open = False


        self.drawer_overlay.opacity = 0

        self.drawer_overlay.disabled = True


        Animation(
            x=-self.drawer_width,
            duration=0.25
        ).start(
            self.drawer
        )



    # -----------------------------------------
    # LOGOUT
    # -----------------------------------------

    def logout(
        self,
        *_ 
    ):

        try:

            if self.app_state:

                self.app_state.logout()


        except Exception as exc:

            print(
                "LOGOUT ERROR:",
                repr(exc)
            )


        if self.manager:

            if self.manager.has_screen(
                "login"
            ):

                self.manager.current = (
                    "login"
                )



    # -----------------------------------------
    # ENTER SCREEN
    # -----------------------------------------

    def on_enter(
        self,
        *_ 
    ):

        try:

            self.refresh()

        except Exception as exc:

            print(
                "DASHBOARD REFRESH ERROR:",
                repr(exc)
            )



    # -----------------------------------------
    # CANVAS UPDATE
    # -----------------------------------------

    def _update_overlay(
        self,
        instance,
        value
    ):

        self.overlay_rect.pos = (
            instance.pos
        )

        self.overlay_rect.size = (
            instance.size
        )



    def _update_header(
        self,
        instance,
        value
    ):

        self.header_rect.pos = (
            instance.pos
        )

        self.header_rect.size = (
            instance.size
        )



    def _update_welcome(
        self,
        instance,
        value
    ):

        self.welcome_rect.pos = (
            instance.pos
        )

        self.welcome_rect.size = (
            instance.size
        )



    def _update_drawer(
        self,
        instance,
        value
    ):

        self.drawer_rect.pos = (
            instance.pos
        )

        self.drawer_rect.size = (
            instance.size
        )



    # -----------------------------------------
    # TEXT RTL
    # -----------------------------------------

    def _sync_text_size(
        self,
        instance,
        value
    ):

        instance.text_size = value
