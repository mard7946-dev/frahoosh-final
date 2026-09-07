from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp


from mobile.config import (
    APP_NAME,
    SCHOOL_NAME,
    PRIMARY,
    SECONDARY,
    WHITE,
)


from mobile.ui import (
    font_name,
    rtl_text,
)



INFO_TEXTS = [

    "فراهوش مدیریت مدرسه را هوشمند و یکپارچه می‌کند.",

    "آیا می‌دانید با فراهوش ارتباط مدرسه و خانواده سریع‌تر می‌شود؟",

    "آیا می‌دانید گزارش‌های آموزشی می‌توانند هوشمند تحلیل شوند؟",

]


MENU_ITEMS_MANAGER = [

    ("مدیریت", "management"),

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



class DashboardScreen(Screen):


    def __init__(self, app_state, **kwargs):

        super().__init__(**kwargs)

        self.app_state = app_state

        self.menu_open = False

        self.info_index = 0

        self.char_index = 0

        self.build()


    def build(self):

        self.root_box = FloatLayout()


        # بک گراند موقت
        # بعداً تصویر نهایی جایگزین می‌شود

        self.root_box.add_widget(
            Label(
                text="",
                size_hint=(1,1)
            )
        )


        self.create_header()


        self.create_info_card()


        self.create_bottom_cards()


        self.add_widget(
            self.root_box
        )


        Clock.schedule_interval(
            self.type_writer,
            0.08
        )


        Animation(
            opacity=1,
            duration=1
        ).start(
            self.root_box
        )

           # =========================
    # HEADER
    # =========================

    def create_header(self):


        self.header_box = BoxLayout(

            orientation="horizontal",

            size_hint=(1, None),

            height=dp(75),

            pos_hint={
                "top":1
            },

            padding=[
                dp(15),
                dp(10)
            ]

        )


        # سه خط واقعی

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

            size_hint_x=None,

            width=dp(60)

        )


        self.menu_button.bind(

            on_release=self.toggle_menu

        )


        self.header_title = Label(

            text=rtl_text(

                f"{APP_NAME}\n"
                f"سامانه هوشمند مدیریت مدرسه\n"
                f"{SCHOOL_NAME}"

            ),

            font_name=font_name(),

            font_size="16sp",

            color=PRIMARY,

            halign="right",

            valign="middle"

        )


        self.header_title.bind(

            size=self.header_title.setter(
                "text_size"
            )

        )


        self.header_box.add_widget(

            self.menu_button

        )


        self.header_box.add_widget(

            self.header_title

        )


        self.root_box.add_widget(

            self.header_box

        )


    # =========================
    # INFO CARD
    # =========================

    def create_info_card(self):


        self.info_card = BoxLayout(

            orientation="vertical",

            size_hint=(0.85, None),

            height=dp(150),

            pos_hint={

                "center_x":0.5,

                "center_y":0.55

            },

            padding=dp(15)

        )


        self.info_title = Label(

            text=rtl_text(

                "✨ آیا می‌دانید..."

            ),

            font_name=font_name(),

            font_size="20sp",

            color=PRIMARY

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

            size=self.info_text.setter(
                "text_size"
            )

        )


        self.info_card.add_widget(

            self.info_title

        )


        self.info_card.add_widget(

            self.info_text

        )


        self.root_box.add_widget(

            self.info_card

        )



    # =========================
    # TYPE WRITER
    # =========================

    def type_writer(self, dt):


        if self.info_index >= len(INFO_TEXTS):

            self.info_index = 0


        text = INFO_TEXTS[
            self.info_index
        ]


        if self.char_index < len(text):

            self.info_text.text = rtl_text(

                text[:self.char_index]

            )

            self.char_index += 1


        else:

            self.char_index = 0

            self.info_index += 1



    # =========================
    # BOTTOM CARDS
    # =========================

    def create_bottom_cards(self):


        bottom = BoxLayout(

            orientation="horizontal",

            spacing=dp(10),

            size_hint=(0.9,None),

            height=dp(80),

            pos_hint={

                "center_x":0.5,

                "y":0.05

            }

        )


        cards = [

            "هوش مصنوعی",

            "کلاس آنلاین",

            "مدیریت هوشمند"

        ]


        for item in cards:


            card = Button(

                text=rtl_text(item),

                font_name=font_name(),

                background_normal="",

                background_color=SECONDARY,

                color=WHITE

            )


            bottom.add_widget(

                card

            )


        self.root_box.add_widget(

            bottom

        )

            # =========================
    # DRAWER MENU
    # =========================

    def toggle_menu(self, *_):

        if self.menu_open:

            self.close_menu()

        else:

            self.open_menu()



    def open_menu(self):


        if hasattr(
            self,
            "drawer"
        ):

            return


        self.drawer = BoxLayout(

            orientation="vertical",

            spacing=dp(6),

            padding=dp(12),

            size_hint=(0.75,1),

            pos_hint={

                "right":1,

                "top":1

            }

        )


        role = "student"


        if self.app_state:

            role = self.app_state.role



        items = []


        if role in (
            "manager",
            "admin"
        ):

            items = MENU_ITEMS_MANAGER


        else:

            items = [

                ("پروفایل من","profile"),

                ("اطلاعات من","info"),

                ("پیام‌ها","messages"),

                ("تنظیمات","settings"),

            ]



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

                on_release=lambda x,t=title,k=key:

                self.open_panel(t,k)

            )


            self.drawer.add_widget(

                btn

            )


        self.root_box.add_widget(

            self.drawer

        )


        self.menu_open = True



        Animation(

            opacity=1,

            duration=0.3

        ).start(

            self.drawer

        )





    def close_menu(self):


        if hasattr(

            self,

            "drawer"

        ):


            self.root_box.remove_widget(

                self.drawer

            )


            self.drawer = None


        self.menu_open = False





    # =========================
    # OPEN MODULE
    # =========================

    def open_panel(
        self,
        title,
        key
    ):


        self.close_menu()


        if key == "management":


            if not self.manager.has_screen(
                "management"
            ):

                from mobile.screens.management import (
                    ManagementScreen
                )


                self.manager.add_widget(

                    ManagementScreen(

                        self.app_state,

                        name="management"

                    )

                )


            self.manager.current = "management"

            return



        # بقیه پنل‌ها فعلاً از مسیر module عبور می‌کنند

        if not self.manager.has_screen(
            "module"
        ):


            from mobile.screens.module import (
                ModuleScreen
            )


            self.manager.add_widget(

                ModuleScreen(

                    self.app_state,

                    name="module"

                )

            )



        module = self.manager.get_screen(
            "module"
        )


        module.show_module(

            title,

            key,

            self.app_state.role

        )


        self.manager.current = "module"

                
                    
                
