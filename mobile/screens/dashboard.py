from kivy.clock import Clock
from kivy.animation import Animation

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp

from kivy.graphics import Color, RoundedRectangle

from mobile.config import (
    APP_NAME,
    SCHOOL_NAME,
    PRIMARY,
    SECONDARY,
    SUCCESS,
    WHITE,
)

from mobile.ui import (
    font_name,
    rtl_text,
)



MENU_ITEMS_MANAGER = [

    ("مدیریت مدرسه", "management"),

    ("معاون آموزشی", "education"),

    ("معاون اجرایی", "executive"),

    ("معاون پرورشی", "cultural"),

    ("مشاوره", "counseling"),

    ("اولیا", "parents"),

    ("دانش‌آموزان", "students"),

    ("مالی", "finance"),

    ("کلاس‌های آنلاین", "online"),

    ("تابلو هوشمند", "smart_board"),

    ("هوش مصنوعی", "ai"),

    ("صندوق پیام‌ها", "messages"),

    ("تنظیمات", "settings"),

    ("درباره برنامه", "about"),

]


INFO_TEXTS = [

    "آیا می‌دانید فراهوش می‌تواند مدیریت مدرسه را هوشمندتر، سریع‌تر و دقیق‌تر کند؟",

    "آیا می‌دانید مدیر مدرسه می‌تواند همه بخش‌های آموزشی و اجرایی را یکپارچه مدیریت کند؟",

    "آیا می‌دانید اولیا می‌توانند ارتباط بهتر و سریع‌تری با مدرسه داشته باشند؟",

    "آیا می‌دانید هوش مصنوعی فراهوش در تحلیل آموزشی به مدرسه کمک می‌کند؟",

    "آیا می‌دانید کلاس آنلاین و تابلو هوشمند بخشی از سامانه یکپارچه فراهوش هستند؟",

]


class RoundedCard(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        with self.canvas.before:

            Color(
                1,
                1,
                1,
                0.90
            )

            self.rect = RoundedRectangle(
                radius=[
                    dp(20)
                ]
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )


    def update_rect(
        self,
        *args
    ):

        self.rect.pos = self.pos
        self.rect.size = self.size



class DashboardScreen(Screen):


    def __init__(
        self,
        app_state,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )

        self.app_state = app_state

        self.text_index = 0

        self.char_index = 0

        self.current_text = ""

        self.menu_open = False

        self.build()

    def build(self):

        root = FloatLayout()


        # =========================
        # BACKGROUND
        # =========================

        with root.canvas.before:

            Color(
                0.94,
                0.97,
                1,
                1
            )

            self.background = RoundedRectangle(
                radius=[
                    dp(0)
                ]
            )


        # =========================
        # HEADER
        # =========================

        self.menu_button = Button(

            text="☰",

            font_size="32sp",

            font_name=font_name(),

            background_normal="",

            background_color=(
                0,
                0,
                0,
                0
            ),

            color=PRIMARY,

            size_hint=(
                None,
                None
            ),

            size=(
                dp(60),
                dp(60)
            ),

            pos_hint={
                "right": 1,
                "top": 1
            }

        )


        self.menu_button.bind(
            on_release=self.toggle_menu
        )


        root.add_widget(
            self.menu_button
        )


        self.title_box = BoxLayout(

            orientation="vertical",

            size_hint=(
                1,
                None
            ),

            height=dp(100),

            pos_hint={
                "center_x":0.5,
                "top":0.95
            }

        )


        title = Label(

            text=rtl_text(
                "سامانه هوشمند مدیریت مدرسه"
            ),

            font_name=font_name(),

            font_size="22sp",

            color=PRIMARY

        )


        school = Label(

            text=rtl_text(
                SCHOOL_NAME
            ),

            font_name=font_name(),

            font_size="15sp",

            color=SECONDARY

        )


        self.title_box.add_widget(
            title
        )

        self.title_box.add_widget(
            school
        )


        root.add_widget(
            self.title_box
        )


        # =========================
        # INFO CARD
        # =========================


        self.info_card = RoundedCard(

            orientation="vertical",

            padding=dp(20),

            spacing=dp(10),

            size_hint=(
                .86,
                None
            ),

            height=dp(180),

            pos_hint={
                "center_x":0.5,
                "center_y":0.55
            }

        )


        self.info_title = Label(

            text=rtl_text(
                "✨ آیا می‌دانید..."
            ),

            font_name=font_name(),

            font_size="18sp",

            color=PRIMARY,

            size_hint_y=None,

            height=dp(40)

        )


        self.info_text = Label(

            text="",

            font_name=font_name(),

            font_size="15sp",

            color=SECONDARY,

            halign="center",

            valign="middle"

        )


        self.info_text.bind(
            size=lambda instance, value:
            setattr(
                instance,
                "text_size",
                value
            )
        )


        self.info_card.add_widget(
            self.info_title
        )


        self.info_card.add_widget(
            self.info_text
        )


        root.add_widget(
            self.info_card
        )


        # =========================
        # FEATURE CARDS
        # =========================


        features = BoxLayout(

            orientation="horizontal",

            spacing=dp(8),

            size_hint=(
                .9,
                None
            ),

            height=dp(80),

            pos_hint={
                "center_x":0.5,
                "y":0.08
            }

        )


        items = [

            "🤖\nهوش مصنوعی",

            "📚\nمدیریت آموزشی",

            "🎥\nکلاس آنلاین",

        ]


        for item in items:

            card = Button(

                text=rtl_text(item),

                font_name=font_name(),

                font_size="13sp",

                background_normal="",

                background_color=(
                    SECONDARY
                ),

                color=WHITE

            )

            features.add_widget(
                card
            )


        root.add_widget(
            features
        )


        self.add_widget(
            root
        )


        Clock.schedule_interval(
            self.type_effect,
            0.08
        )


    # =========================
    # TYPE EFFECT
    # =========================

    def type_effect(
        self,
        dt
    ):

        if self.text_index >= len(INFO_TEXTS):

            self.text_index = 0


        full_text = INFO_TEXTS[
            self.text_index
        ]


        if self.char_index <= len(full_text):

            self.current_text = (
                full_text[:self.char_index]
            )

            self.info_text.text = rtl_text(
                self.current_text
            )

            self.char_index += 1


        else:

            self.char_index = 0

            self.text_index += 1



    # =========================
    # SIDE MENU
    # =========================

    def toggle_menu(
        self,
        *_ 
    ):

        if self.menu_open:

            self.close_menu()

        else:

            self.open_menu()



    def open_menu(
        self
    ):

        self.menu_open = True


        self.menu_box = BoxLayout(

            orientation="vertical",

            spacing=dp(6),

            padding=dp(12),

            size_hint=(
                None,
                1
            ),

            width=dp(280),

            pos_hint={
                "left":0,
                "top":1
            }

        )


        with self.menu_box.canvas.before:

            Color(
                1,
                1,
                1,
                .96
            )

            self.menu_background = RoundedRectangle(
                radius=[
                    dp(20)
                ]
            )


        self.menu_box.bind(
            pos=self.update_menu_bg,
            size=self.update_menu_bg
        )


        role = "student"


        if self.app_state:

            role = getattr(
                self.app_state,
                "role",
                "student"
            )


        # مدیر همه را می‌بیند

        if role in [
            "manager",
            "admin"
        ]:

            items = MENU_ITEMS_MANAGER


        else:

            items = self.get_user_menu(
                role
            )



        for title, key in items:

            btn = Button(

                text=rtl_text(title),

                font_name=font_name(),

                background_normal="",

                background_color=SECONDARY,

                color=WHITE,

                size_hint_y=None,

                height=dp(48)

            )


            btn.bind(
                on_release=lambda x, k=key, t=title:
                self.select_menu(
                    t,
                    k
                )
            )


            self.menu_box.add_widget(
                btn
            )


        self.add_widget(
            self.menu_box
        )


        Animation(
            x=0,
            duration=.25
        ).start(
            self.menu_box
        )



    def update_menu_bg(
        self,
        *args
    ):

        if hasattr(
            self,
            "menu_background"
        ):

            self.menu_background.pos = (
                self.menu_box.pos
            )

            self.menu_background.size = (
                self.menu_box.size
            )



    def close_menu(
        self
    ):

        if hasattr(
            self,
            "menu_box"
        ):

            self.remove_widget(
                self.menu_box
            )


        self.menu_open = False



    # =========================
    # USER MENUS
    # =========================

    def get_user_menu(
        self,
        role
    ):


        menus = {

            "student":[

                ("پروفایل من","profile"),

                ("کلاس من","classes"),

                ("برنامه هفتگی","schedule"),

                ("نمرات","grades"),

                ("کارنامه","report"),

                ("کلاس آنلاین","online")

            ],


            "parent":[

                ("فرزند من","child"),

                ("وضعیت تحصیلی","status"),

                ("پرداخت‌ها","payments"),

                ("پیام‌های مدرسه","messages")

            ],


            "teacher":[

                ("کلاس‌های من","classes"),

                ("ثبت نمرات","grades"),

                ("حضور و غیاب","attendance"),

                ("پیام‌ها","messages")

            ]

        }


        return menus.get(
            role,
            menus["student"]
        )



    # =========================
    # MENU CLICK
    # =========================

    def select_menu(
        self,
        title,
        key
    ):

        self.close_menu()


        print(
            "OPEN PANEL:",
            title,
            key
        )


        # فعلاً اتصال پنل‌ها
        # در مرحله بعد اضافه می‌شود



    # =========================
    # REFRESH
    # =========================

    def on_pre_enter(
        self
    ):

        self.text_index = 0

        self.char_index = 0


