from threading import Thread

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from mobile.config import (
    APP_NAME,
    SCHOOL_NAME,
    SCHOOL_YEAR,
    PRIMARY,
    SECONDARY,
    SUCCESS,
    ERROR,
    WHITE,
)

from mobile.ui import (
    font_name,
    rtl_text,
)


MODULE_TITLES = {

    "management": "مدیریت",
    "educational": "معاون آموزشی",
    "executive": "معاون اجرایی",
    "cultural": "معاون پرورشی",
    "advisor": "مشاوره",

    "teacher": "پنل دبیر",
    "teachers": "دبیران",

    "student": "پنل دانش‌آموز",
    "students": "دانش‌آموزان",

    "parent": "پنل اولیا",
    "parents": "اولیا",

    "finance": "مالی",
    "payment": "پرداخت آنلاین",

    "online": "کلاس‌های آنلاین",

    "smart_board": "تابلو هوشمند",

    "ai": "دستیار هوش مصنوعی",

    "messages": "صندوق پیام‌ها",

    "settings": "تنظیمات",

    "reports": "گزارش‌ها",

    "schedule": "برنامه هفتگی",

    "student_info": "وضعیت تحصیلی",
}


MODULE_TABLES = {

    "students": [
        "students",
        "student_records",
    ],

    "parents": [
        "parents",
        "parent_records",
    ],

    "teachers": [
        "teachers",
        "staff",
    ],

    "finance": [
        "payment_records",
        "financial_records",
    ],

    "payment": [
        "payment_records",
    ],

    "online": [
        "online_classes",
        "classes",
    ],

    "smart_board": [
        "smart_board_content",
        "smart_board",
    ],

    "messages": [
        "messages",
        "message_records",
    ],

    "reports": [
        "reports",
        "report_cards",
    ],

    "settings": [
        "school_settings",
        "account_settings",
    ],
}


class ModuleScreen(Screen):


    def __init__(
        self,
        app_state,
        **kwargs
    ):

        super().__init__(
            **kwargs
        )

        self.app_state = app_state

        self.module_key = ""

        self.loading_label = None

        self._build()


    # ============================
    # UI
    # ============================


    def _build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=dp(14),
            spacing=dp(10),
        )


        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(58),
            spacing=dp(8),
        )


        self.back_button = Button(
            text=rtl_text(
                "‹ داشبورد"
            ),
            font_name=font_name(),
            font_size="14sp",
            background_normal="",
            background_color=PRIMARY,
            color=WHITE,
            size_hint_x=None,
            width=dp(110),
        )


        self.back_button.bind(
            on_release=self.go_back
        )


        self.title_label = Label(
            text=rtl_text(
                APP_NAME
            ),
            font_name=font_name(),
            font_size="22sp",
            bold=True,
            color=PRIMARY,
            halign="right",
            valign="middle",
        )


        self.title_label.bind(
            size=self._sync_text_size
        )


        header.add_widget(
            self.back_button
        )


        header.add_widget(
            self.title_label
        )


        root.add_widget(
            header
        )


        self.status_label = Label(
            text="",
            font_name=font_name(),
            font_size="13sp",
            color=SECONDARY,
            size_hint_y=None,
            height=dp(45),
            halign="right",
            valign="middle",
        )


        self.status_label.bind(
            size=self._sync_text_size
        )


        root.add_widget(
            self.status_label
        )


        scroll = ScrollView(
            do_scroll_x=False
        )


        self.body = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=dp(6),
            size_hint_y=None,
        )


        self.body.bind(
            minimum_height=
            self.body.setter(
                "height"
            )
        )


        scroll.add_widget(
            self.body
        )


        root.add_widget(
            scroll
        )


        self.add_widget(
            root
        )



    # ============================
    # ROUTING
    # ============================


    def set_module(
        self,
        key
    ):

        self.show_module(
            key
        )


    def load_module(
        self,
        key
    ):

        self.show_module(
            key
        )


    def show_module(
        self,
        key
    ):

        try:

            self.module_key = (
                str(
                    key or ""
                )
                .strip()
                .lower()
            )


            title = MODULE_TITLES.get(
                self.module_key,
                "فراهوش"
            )


            self.title_label.text = rtl_text(
                title
            )


            self.body.clear_widgets()


            self.status_label.text = rtl_text(
                "در حال آماده‌سازی..."
            )


            self._dispatch_module(
                self.module_key
            )


        except Exception as exc:

            print(
                "SHOW MODULE ERROR:",
                repr(exc)
            )

            self._show_error(
                "باز کردن این بخش با خطا مواجه شد."
            )


    def _dispatch_module(
        self,
        key
    ):

        builders = {

            "management": self._management,

            "educational": self._educational,

            "executive": self._executive,

            "cultural": self._cultural,

            "advisor": self._advisor,

            "teacher": self._teacher,

            "teachers": self._teachers,

            "student": self._student,

            "students": self._students,

            "parent": self._parent,

            "parents": self._parents,

            "finance": self._finance,

            "payment": self._payment,

            "online": self._online,

            "smart_board": self._smart_board,

            "ai": self._ai,

            "messages": self._messages,

            "settings": self._settings,

            "reports": self._reports,

            "schedule": self._schedule,

            "student_info": self._student_info,
        }


        builder = builders.get(
            key
        )


        if builder:

            builder()

        else:

            self._generic(
                key
            )

    # ============================
    # COMMON COMPONENTS
    # ============================


    def _add_title(
        self,
        text
    ):

        label = Label(
            text=rtl_text(text),
            font_name=font_name(),
            font_size="20sp",
            bold=True,
            color=PRIMARY,
            size_hint_y=None,
            height=dp(52),
            halign="right",
            valign="middle",
        )

        label.bind(
            size=self._sync_text_size
        )

        self.body.add_widget(
            label
        )


    def _add_info(
        self,
        text,
        height=90
    ):

        label = Label(
            text=rtl_text(text),
            font_name=font_name(),
            font_size="14sp",
            color=SECONDARY,
            size_hint_y=None,
            height=dp(height),
            halign="right",
            valign="top",
        )

        label.bind(
            size=self._sync_text_size
        )

        self.body.add_widget(
            label
        )


    def _button(
        self,
        text,
        callback,
        color=PRIMARY
    ):

        btn = Button(
            text=rtl_text(text),
            font_name=font_name(),
            font_size="15sp",
            background_normal="",
            background_color=color,
            color=WHITE,
            size_hint_y=None,
            height=dp(50),
        )

        btn.bind(
            on_release=callback
        )

        self.body.add_widget(
            btn
        )


    def _show_error(
        self,
        text
    ):

        self.status_label.text = rtl_text(
            text
        )

        self.status_label.color = ERROR



    # ============================
    # PANELS
    # ============================


    def _management(self):

        self._add_title(
            "مدیریت مدرسه"
        )

        self._add_info(
            f"سامانه هوشمند مدیریت مدرسه\n"
            f"{SCHOOL_NAME}\n"
            f"سال تحصیلی: {SCHOOL_YEAR}",
            110
        )

        self._button(
            "دانش‌آموزان",
            lambda *_:
            self.show_module(
                "students"
            )
        )

        self._button(
            "دبیران",
            lambda *_:
            self.show_module(
                "teachers"
            )
        )

        self._button(
            "امور مالی",
            lambda *_:
            self.show_module(
                "finance"
            )
        )

        self._button(
            "تنظیمات",
            lambda *_:
            self.show_module(
                "settings"
            )
        )


        self.status_label.text = rtl_text(
            "پنل مدیریت فعال است."
        )


    def _educational(self):

        self._add_title(
            "معاون آموزشی"
        )

        self._add_info(
            "مدیریت کلاس‌ها، دبیران، برنامه آموزشی و گزارش‌ها."
        )


        self._button(
            "دانش‌آموزان",
            lambda *_:
            self.show_module(
                "students"
            )
        )


        self._button(
            "دبیران",
            lambda *_:
            self.show_module(
                "teachers"
            )
        )


        self._button(
            "کلاس آنلاین",
            lambda *_:
            self.show_module(
                "online"
            )
        )


    def _executive(self):

        self._add_title(
            "معاون اجرایی"
        )

        self._add_info(
            "مدیریت ثبت‌نام، پرونده‌ها و اطلاعات اجرایی مدرسه."
        )


        self._button(
            "دانش‌آموزان",
            lambda *_:
            self.show_module(
                "students"
            )
        )


        self._button(
            "اولیا",
            lambda *_:
            self.show_module(
                "parents"
            )
        )


    def _cultural(self):

        self._add_title(
            "معاون پرورشی"
        )

        self._add_info(
            "فعالیت‌های پرورشی و ارتباط با دانش‌آموزان."
        )


        self._button(
            "تابلو هوشمند",
            lambda *_:
            self.show_module(
                "smart_board"
            )
        )


        self._button(
            "دانش‌آموزان",
            lambda *_:
            self.show_module(
                "students"
            )
        )


    def _advisor(self):

        self._add_title(
            "مشاوره"
        )

        self._add_info(
            "پیگیری وضعیت آموزشی و مشاوره دانش‌آموزان."
        )


        self._button(
            "دانش‌آموزان",
            lambda *_:
            self.show_module(
                "students"
            )
        )


        self._button(
            "اولیا",
            lambda *_:
            self.show_module(
                "parents"
            )
        )


    def _teacher(self):

        self._add_title(
            "پنل دبیر"
        )

        self._add_info(
            "مدیریت کلاس‌ها، محتوا و ارتباط آموزشی."
        )


        self._button(
            "کلاس آنلاین",
            lambda *_:
            self.show_module(
                "online"
            )
        )


        self._button(
            "تابلو هوشمند",
            lambda *_:
            self.show_module(
                "smart_board"
            )
        )



    def _student(self):

        self._add_title(
            "پنل دانش‌آموز"
        )

        self._add_info(
            "برنامه هفتگی، وضعیت تحصیلی، پرداخت و کلاس آنلاین."
        )


        self._button(
            "برنامه هفتگی",
            lambda *_:
            self.show_module(
                "schedule"
            )
        )


        self._button(
            "وضعیت تحصیلی",
            lambda *_:
            self.show_module(
                "student_info"
            )
        )


        self._button(
            "پرداخت آنلاین",
            lambda *_:
            self.show_module(
                "payment"
            ),
            SUCCESS
        )


        self._button(
            "کلاس آنلاین",
            lambda *_:
            self.show_module(
                "online"
            )
        )



    def _parent(self):

        self._add_title(
            "پنل اولیا"
        )


        self._add_info(
            "مشاهده وضعیت تحصیلی فرزند و خدمات مدرسه."
        )


        self._button(
            "وضعیت تحصیلی",
            lambda *_:
            self.show_module(
                "student_info"
            )
        )


        self._button(
            "پرداخت آنلاین",
            lambda *_:
            self.show_module(
                "payment"
            ),
            SUCCESS
        )


        self._button(
            "کلاس آنلاین",
            lambda *_:
            self.show_module(
                "online"
            )
        )



    def _teachers(self):

        self._add_title(
            "دبیران"
        )

        self._load_table(
            [
                "teachers",
                "staff",
            ]
        )


    def _students(self):

        self._add_title(
            "دانش‌آموزان"
        )

        self._load_table(
            [
                "students",
                "student_records",
            ]
        )


    def _parents(self):

        self._add_title(
            "اولیا"
        )

        self._load_table(
            [
                "parents",
                "parent_records",
            ]
        )

    def _sync_text_size(
        self,
        instance,
        value
    ):

        instance.text_size = value
            
            
