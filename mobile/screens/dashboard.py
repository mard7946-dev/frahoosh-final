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

    ("درباره برنامه", "about"),

]



ROLE_MENU = {


    "executive": [

        ("معاون اجرایی", "executive"),

        ("دانش‌آموزان", "students"),

        ("اولیا", "parents"),

        ("پیام‌ها", "messages"),

        ("تنظیمات", "settings"),

        ("درباره برنامه", "about"),

    ],


    "educational": [

        ("معاون آموزشی", "educational"),

        ("دانش‌آموزان", "students"),

        ("دبیران", "teachers"),

        ("کلاس آنلاین", "online"),

        ("تابلو هوشمند", "smart_board"),

        ("گزارش‌ها", "reports"),

        ("پیام‌ها", "messages"),

        ("درباره برنامه", "about"),

    ],


    "cultural": [

        ("معاون پرورشی", "cultural"),

        ("دانش‌آموزان", "students"),

        ("تابلو هوشمند", "smart_board"),

        ("پیام‌ها", "messages"),

        ("درباره برنامه", "about"),

    ],


    "advisor": [

        ("مشاوره", "advisor"),

        ("دانش‌آموزان", "students"),

        ("اولیا", "parents"),

        ("پیام‌ها", "messages"),

        ("درباره برنامه", "about"),

    ],


    "teacher": [

        ("پنل دبیر", "teacher"),

        ("دانش‌آموزان", "students"),

        ("کلاس آنلاین", "online"),

        ("تابلو هوشمند", "smart_board"),

        ("پیام‌ها", "messages"),

        ("درباره برنامه", "about"),

    ],


    "student": [

        ("پنل دانش‌آموز", "student"),

        ("برنامه هفتگی", "schedule"),

        ("وضعیت تحصیلی", "student_info"),

        ("پرداخت آنلاین", "payment"),

        ("کلاس آنلاین", "online"),

        ("تابلو هوشمند", "smart_board"),

        ("پیام‌ها", "messages"),

        ("درباره برنامه", "about"),

    ],


    "parent": [

        ("پنل اولیا", "parent"),

        ("وضعیت تحصیلی فرزند", "student_info"),

        ("پرداخت آنلاین", "payment"),

        ("کلاس آنلاین", "online"),

        ("تابلو هوشمند", "smart_board"),

        ("پیام‌ها", "messages"),

        ("درباره برنامه", "about"),

    ],

}




class HamburgerButton(Widget):


    def __init__(
        self,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )


        with self.canvas:

            self.line_color = Color(
                1,
                1,
                1,
                1
            )


            self.line1 = Line(
                width=2
            )


            self.line2 = Line(
                width=2
            )


            self.line3 = Line(
                width=2
            )


        self.bind(
            pos=self._update,
            size=self._update
        )



    def _update(
        self,
        *_ 
    ):

        left = (
            self.x
            + self.width * 0.2
        )

        right = (
            self.x
            + self.width * 0.8
        )


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


    def __init__(
        self,
        app_state,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )


        self.app_state = app_state

        self.drawer_open = False

        self._build_ui()

    def _build_ui(self):

        self.clear_widgets()


        root = FloatLayout()



        # -------------------------
        # Background
        # -------------------------

        self.background = Image(

            source=BACKGROUND_PATH,

            allow_stretch=True,

            keep_ratio=False,

            size_hint=(1, 1),

            pos_hint={
                "x": 0,
                "y": 0
            },

        )


        root.add_widget(
            self.background
        )



        # -------------------------
        # Dark Overlay
        # -------------------------

        self.overlay = Widget()


        with self.overlay.canvas:

            self.overlay_color = Color(

                0.02,
                0.08,
                0.15,
                0.25

            )


            self.overlay_rect = Rectangle()



        self.overlay.bind(

            pos=self._update_overlay,

            size=self._update_overlay

        )


        root.add_widget(
            self.overlay
        )



        # -------------------------
        # Header
        # -------------------------

        self.header = FloatLayout(

            size_hint=(1, None),

            height=dp(145),

            pos_hint={
                "top": 1
            }

        )


        with self.header.canvas:

            self.header_color = Color(

                0.02,
                0.15,
                0.28,
                0.90

            )


            self.header_rect = RoundedRectangle()



        self.header.bind(

            pos=self._update_header,

            size=self._update_header

        )


        root.add_widget(
            self.header
        )



        self.menu_button = HamburgerButton(

            size_hint=(None, None),

            size=(

                dp(60),

                dp(60)

            ),

            pos_hint={

                "right":0.97,

                "top":0.90

            }

        )


        self.menu_button.bind(

            on_touch_down=self._hamburger_touch

        )


        self.header.add_widget(

            self.menu_button

        )



        self.title_label = Label(

            text=rtl_text(

                "سامانه هوشمند مدیریت مدرسه"

            ),

            font_name=font_name(),

            font_size="22sp",

            bold=True,

            color=(

                1,

                1,

                1,

                1

            ),

            halign="right",

            valign="middle",

            size_hint=(0.75, None),

            height=dp(45),

            pos_hint={

                "right":0.90,

                "top":0.75

            }

        )


        self.title_label.bind(

            size=self._sync_text_size

        )


        self.header.add_widget(

            self.title_label

        )



        self.school_label = Label(

            text=rtl_text(

                SCHOOL_NAME

            ),

            font_name=font_name(),

            font_size="14sp",

            color=(

                0.85,

                0.95,

                1,

                1

            ),

            halign="right",

            valign="middle",

            size_hint=(0.75,None),

            height=dp(35),

            pos_hint={

                "right":0.90,

                "top":0.45

            }

        )


        self.school_label.bind(

            size=self._sync_text_size

        )


        self.header.add_widget(

            self.school_label

        )



        # -------------------------
        # Welcome Card
        # -------------------------

        self.welcome_card = FloatLayout(

            size_hint=(0.90,None),

            height=dp(160),

            pos_hint={

                "center_x":0.5,

                "top":0.76

            }

        )


        with self.welcome_card.canvas:

            self.welcome_color = Color(

                1,

                1,

                1,

                0.93

            )


            self.welcome_rect = RoundedRectangle(

                radius=[dp(22)]

            )


        self.welcome_card.bind(

            pos=self._update_welcome,

            size=self._update_welcome

        )


        root.add_widget(

            self.welcome_card

        )



        self.welcome_title = Label(

            text=rtl_text(

                "خوش آمدید"

            ),

            font_name=font_name(),

            font_size="22sp",

            bold=True,

            color=(

                0.02,

                0.18,

                0.32,

                1

            ),

            halign="right",

            valign="middle",

            size_hint=(0.85,None),

            height=dp(45),

            pos_hint={

                "right":0.94,

                "top":0.82

            }

        )


        self.welcome_title.bind(

            size=self._sync_text_size

        )


        self.welcome_card.add_widget(

            self.welcome_title

        )



        self.role_label = Label(

            text="",

            font_name=font_name(),

            font_size="16sp",

            color=(

                0.1,

                0.3,

                0.45,

                1

            ),

            halign="right",

            valign="middle",

            size_hint=(0.85,None),

            height=dp(38),

            pos_hint={

                "right":0.94,

                "top":0.53

            }

        )


        self.role_label.bind(

            size=self._sync_text_size

        )


        self.welcome_card.add_widget(

            self.role_label

        )



        self.status_label = Label(

            text=rtl_text(

                "سامانه آماده استفاده است"

            ),

            font_name=font_name(),

            font_size="14sp",

            color=(

                0.1,

                0.45,

                0.3,

                1

            ),

            halign="right",

            valign="middle",

            size_hint=(0.85,None),

            height=dp(35),

            pos_hint={

                "right":0.94,

                "top":0.25

            }

        )


        self.status_label.bind(

            size=self._sync_text_size

        )


        self.welcome_card.add_widget(

            self.status_label

        )

        # -------------------------
        # Drawer Overlay
        # -------------------------

        self.drawer_overlay = Button(

            text="",

            background_normal="",

            background_color=(

                0,

                0,

                0,

                0.45

            ),

            size_hint=(1,1),

            opacity=0,

            disabled=True,

        )


        self.drawer_overlay.bind(

            on_release=self.close_drawer

        )


        root.add_widget(

            self.drawer_overlay

        )



        # -------------------------
        # Drawer
        # -------------------------

        self.drawer = FloatLayout(

            size_hint=(None,1),

            width=dp(320),

            x=-dp(320)

        )


        with self.drawer.canvas:

            self.drawer_color = Color(

                0.02,

                0.09,

                0.17,

                1

            )


            self.drawer_rect = RoundedRectangle()



        self.drawer.bind(

            pos=self._update_drawer,

            size=self._update_drawer

        )


        root.add_widget(

            self.drawer

        )


        self._build_drawer()



        self.add_widget(

            root

        )



    def _build_drawer(self):


        self.drawer.clear_widgets()



        title = Label(

            text=rtl_text(

                APP_NAME

            ),

            font_name=font_name(),

            font_size="26sp",

            bold=True,

            color=(1,1,1,1),

            size_hint=(1,None),

            height=dp(60),

            pos_hint={

                "top":0.98

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

            size_hint=(1,None),

            height=dp(40),

            pos_hint={

                "top":0.88

            }

        )


        self.drawer.add_widget(

            self.menu_role

        )



        self.menu_scroll = ScrollView(

            size_hint=(0.95,0.68),

            pos_hint={

                "center_x":0.5,

                "top":0.78

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

                0.6,

                0.1,

                0.15,

                1

            ),

            color=(1,1,1,1),

            size_hint=(0.88,None),

            height=dp(50),

            pos_hint={

                "center_x":0.5,

                "y":0.03

            }

        )


        self.logout_button.bind(

            on_release=self.logout

        )


        self.drawer.add_widget(

            self.logout_button

        )



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

                color=(1,1,1,1),

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
