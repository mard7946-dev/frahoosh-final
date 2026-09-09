from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

from mobile.config import (
    APP_NAME,
    SCHOOL_NAME,
    PRIMARY,
    SECONDARY,
    SUCCESS,
    ERROR,
    WHITE,
)

from mobile.ui import font_name, rtl_text


MODULE_TITLES = {
    "management": "مدیریت مدرسه",
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
    "finance": "امور مالی",
    "payment": "پرداخت‌ها",
    "online": "کلاس‌های آنلاین",
    "smart_board": "تابلو هوشمند",
    "ai": "هوش مصنوعی",
    "reports": "گزارش‌ها",
    "messages": "پیام‌ها",
    "settings": "تنظیمات",
    "schedule": "برنامه هفتگی",
    "student_info": "وضعیت تحصیلی",
    "about": "درباره فراهوش",
}


def safe_str(value, default=""):
    if value is None:
        return default

    try:
        return str(value)
    except Exception:
        return default


def make_label(
    text="",
    font_size="14sp",
    color=SECONDARY,
    bold=False,
    height=dp(40),
    halign="right",
):
    label = Label(
        text=rtl_text(safe_str(text)),
        font_name=font_name(),
        font_size=font_size,
        color=color,
        bold=bold,
        halign=halign,
        valign="middle",
        size_hint_y=None,
        height=height,
    )

    label.bind(
        size=lambda obj, value:
        setattr(obj, "text_size", value)
    )

    return label


def make_button(
    text,
    callback=None,
    height=dp(48),
    background_color=None,
):
    if background_color is None:
        background_color = (
            0.05,
            0.22,
            0.34,
            1,
        )

    button = Button(
        text=rtl_text(safe_str(text)),
        font_name=font_name(),
        font_size="14sp",
        background_normal="",
        background_color=background_color,
        color=WHITE,
        size_hint_y=None,
        height=height,
    )

    if callback is not None:
        button.bind(on_release=callback)

    return button


class ModuleScreen(Screen):

    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)

        self.app_state = app_state
        self.module_key = ""
        self.module_title = ""

        self.content = None
        self.status_label = None
        self.title_label = None

        self._build_base()


    # =====================================================
    # BASE UI
    # =====================================================

    def _build_base(self):

        self.clear_widgets()

        root = FloatLayout()


        card = BoxLayout(
            orientation="vertical",
            padding=[
                dp(18),
                dp(18),
                dp(18),
                dp(18),
            ],
            spacing=dp(10),
            size_hint=(0.94, 0.92),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5,
            },
        )


        with card.canvas.before:
            Color(
                1,
                1,
                1,
                0.97,
            )

            self.card_rect = RoundedRectangle(
                radius=[dp(22)]
            )


        card.bind(
            pos=self._update_card,
            size=self._update_card,
        )


        root.add_widget(card)


        # -------------------------------------------------
        # HEADER
        # -------------------------------------------------

        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(58),
            spacing=dp(8),
        )


        self.back_button = make_button(
            "بازگشت",
            self._go_back,
            height=dp(48),
            background_color=(
                0.25,
                0.30,
                0.36,
                1,
            ),
        )

        header.add_widget(
            self.back_button
        )


        self.title_label = make_label(
            APP_NAME,
            font_size="21sp",
            color=PRIMARY,
            bold=True,
            height=dp(48),
        )

        header.add_widget(
            self.title_label
        )


        card.add_widget(header)


        # -------------------------------------------------
        # STATUS
        # -------------------------------------------------

        self.status_label = make_label(
            "",
            font_size="13sp",
            color=SECONDARY,
            height=dp(34),
        )

        card.add_widget(
            self.status_label
        )


        # -------------------------------------------------
        # SCROLL CONTENT
        # -------------------------------------------------

        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
        )


        self.content = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=[
                dp(4),
                dp(4),
                dp(4),
                dp(20),
            ],
            size_hint_y=None,
        )


        self.content.bind(
            minimum_height=
            self.content.setter("height")
        )


        scroll.add_widget(
            self.content
        )

        card.add_widget(
            scroll
        )


        self.add_widget(root)


    def _update_card(self, instance, value):
        self.card_rect.pos = instance.pos
        self.card_rect.size = instance.size


    # =====================================================
    # MODULE LOADING
    # =====================================================

    def set_module(self, module_key):
        return self.show_module(
            module_key
        )


    def load_module(self, module_key):
        return self.show_module(
            module_key
        )


    def show_module(self, module_key):

        module_key = safe_str(
            module_key
        ).strip().lower()


        if not module_key:
            module_key = "about"


        self.module_key = module_key


        self.module_title = MODULE_TITLES.get(
            module_key,
            "بخش مورد نظر",
        )


        if self.title_label:
            self.title_label.text = rtl_text(
                self.module_title
            )


        if self.status_label:
            self.status_label.text = ""


        if self.content:
            self.content.clear_widgets()


        try:

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

                "reports": self._reports,

                "messages": self._messages,

                "settings": self._settings,

                "schedule": self._schedule,

                "student_info": self._student_info,

                "about": self._about,
            }


            builder = builders.get(
                module_key
            )


            if builder is None:
                self._unknown_module(
                    module_key
                )
            else:
                builder()


        except Exception as exc:

            print(
                "MODULE LOAD ERROR:",
                repr(exc),
            )


            self._set_status(
                "خطا در بارگذاری این بخش.",
                ERROR,
            )


            if self.content:

                self.content.clear_widgets()

                self.content.add_widget(
                    make_label(
                        f"خطا: {exc}",
                        font_size="13sp",
                        color=ERROR,
                        height=dp(80),
                    )
                )


        return True


    def refresh(self):

        if self.module_key:
            return self.show_module(
                self.module_key
            )

        return False


    # =====================================================
    # COMMON UI HELPERS
    # =====================================================

    def _section_title(self, text):

        label = make_label(
            text,
            font_size="17sp",
            color=PRIMARY,
            bold=True,
            height=dp(48),
        )

        self.content.add_widget(
            label
        )

        return label


    def _info_card(
        self,
        title,
        value="",
    ):

        box = BoxLayout(
            orientation="vertical",
            spacing=dp(4),
            padding=dp(10),
            size_hint_y=None,
            height=dp(76),
        )


        with box.canvas.before:

            Color(
                0.94,
                0.97,
                0.99,
                1,
            )

            rect = RoundedRectangle(
                radius=[dp(12)]
            )


        box.bind(
            pos=lambda obj, value:
            setattr(
                rect,
                "pos",
                value,
            ),

            size=lambda obj, value:
            setattr(
                rect,
                "size",
                value,
            ),
        )


        box.add_widget(
            make_label(
                title,
                font_size="13sp",
                color=SECONDARY,
                height=dp(25),
            )
        )


        box.add_widget(
            make_label(
                value,
                font_size="15sp",
                color=PRIMARY,
                bold=True,
                height=dp(30),
            )
        )


        self.content.add_widget(
            box
        )

        return box


    def _action_row(self, actions):

        row = BoxLayout(
            orientation="horizontal",
            spacing=dp(8),
            size_hint_y=None,
            height=dp(50),
        )


        for title, callback in actions:

            row.add_widget(
                make_button(
                    title,
                    callback,
                    height=dp(48),
                )
            )


        self.content.add_widget(
            row
        )

        return row


    def _placeholder(self, text):

        self.content.add_widget(
            make_label(
                text,
                font_size="14sp",
                color=SECONDARY,
                height=dp(90),
            )
        )


    def _set_status(
        self,
        text,
        color=SECONDARY,
    ):

        if self.status_label:

            self.status_label.text = rtl_text(
                safe_str(text)
            )

            self.status_label.color = color


    # =====================================================
    # NAVIGATION
    # =====================================================

    def _go_back(self, *_args):

        if (
            self.manager
            and self.manager.has_screen(
                "dashboard"
            )
        ):

            self.manager.current = (
                "dashboard"
            )


    def _unknown_module(self, module_key):

        self._set_status(
            "این بخش در نسخه فعلی تعریف نشده است.",
            ERROR,
        )

        self._placeholder(
            f"بخش «{module_key}» هنوز پیاده‌سازی نشده است."
        )

    # =====================================================
    # MANAGEMENT
    # =====================================================

    def _management(self):

        self._section_title(
            "مدیریت مدرسه"
        )

        self._info_card(
            "مدرسه",
            SCHOOL_NAME
        )

        role = ""

        try:
            role = safe_str(
                self.app_state.role,
                "مدیر"
            )
        except Exception:
            role = "مدیر"

        self._info_card(
            "نقش کاربر",
            role
        )

        self._section_title(
            "دسترسی‌های مدیریت"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "دبیران",
                lambda *_:
                self.show_module("teachers")
            ),
        ])

        self._action_row([
            (
                "اولیا",
                lambda *_:
                self.show_module("parents")
            ),
            (
                "امور مالی",
                lambda *_:
                self.show_module("finance")
            ),
        ])

        self._action_row([
            (
                "کلاس آنلاین",
                lambda *_:
                self.show_module("online")
            ),
            (
                "گزارش‌ها",
                lambda *_:
                self.show_module("reports")
            ),
        ])

        self._action_row([
            (
                "تنظیمات",
                lambda *_:
                self.show_module("settings")
            ),
        ])


    # =====================================================
    # EDUCATIONAL
    # =====================================================

    def _educational(self):

        self._section_title(
            "معاون آموزشی"
        )

        self._info_card(
            "وظیفه اصلی",
            "مدیریت و پیگیری امور آموزشی مدرسه"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "دبیران",
                lambda *_:
                self.show_module("teachers")
            ),
        ])

        self._action_row([
            (
                "برنامه هفتگی",
                lambda *_:
                self.show_module("schedule")
            ),
            (
                "گزارش تحصیلی",
                lambda *_:
                self.show_module("student_info")
            ),
        ])

        self._action_row([
            (
                "گزارش‌ها",
                lambda *_:
                self.show_module("reports")
            ),
        ])


    # =====================================================
    # EXECUTIVE
    # =====================================================

    def _executive(self):

        self._section_title(
            "معاون اجرایی"
        )

        self._info_card(
            "مدیریت اجرایی",
            "ثبت و پیگیری اطلاعات اجرایی مدرسه"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "اولیا",
                lambda *_:
                self.show_module("parents")
            ),
        ])

        self._action_row([
            (
                "امور مالی",
                lambda *_:
                self.show_module("finance")
            ),
            (
                "تنظیمات",
                lambda *_:
                self.show_module("settings")
            ),
        ])


    # =====================================================
    # CULTURAL
    # =====================================================

    def _cultural(self):

        self._section_title(
            "معاون پرورشی"
        )

        self._info_card(
            "بخش پرورشی",
            "مدیریت فعالیت‌های فرهنگی و پرورشی"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "پیام‌ها",
                lambda *_:
                self.show_module("messages")
            ),
        ])

        self._action_row([
            (
                "تابلو هوشمند",
                lambda *_:
                self.show_module("smart_board")
            ),
            (
                "گزارش‌ها",
                lambda *_:
                self.show_module("reports")
            ),
        ])


    # =====================================================
    # ADVISOR
    # =====================================================

    def _advisor(self):

        self._section_title(
            "مشاوره"
        )

        self._info_card(
            "خدمات مشاوره",
            "پیگیری وضعیت دانش‌آموزان"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "وضعیت تحصیلی",
                lambda *_:
                self.show_module("student_info")
            ),
        ])

        self._action_row([
            (
                "گزارش‌ها",
                lambda *_:
                self.show_module("reports")
            ),
        ])


    # =====================================================
    # TEACHER PANEL
    # =====================================================

    def _teacher(self):

        self._section_title(
            "پنل دبیر"
        )

        display_name = ""

        try:
            display_name = safe_str(
                self.app_state.display_name
            )
        except Exception:
            display_name = ""

        if not display_name:
            display_name = "دبیر"

        self._info_card(
            "کاربر",
            display_name
        )

        self._action_row([
            (
                "برنامه هفتگی",
                lambda *_:
                self.show_module("schedule")
            ),
            (
                "کلاس آنلاین",
                lambda *_:
                self.show_module("online")
            ),
        ])

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "گزارش‌ها",
                lambda *_:
                self.show_module("reports")
            ),
        ])

        self._action_row([
            (
                "پیام‌ها",
                lambda *_:
                self.show_module("messages")
            ),
        ])


    # =====================================================
    # TEACHERS
    # =====================================================

    def _teachers(self):

        self._section_title(
            "دبیران"
        )

        self._set_status(
            "در حال دریافت فهرست دبیران..."
        )

        self._load_table(
            ["teachers", "staff"],
            "دبیران"
        )


    # =====================================================
    # STUDENT PANEL
    # =====================================================

    def _student(self):

        self._section_title(
            "پنل دانش‌آموز"
        )

        display_name = ""

        try:
            display_name = safe_str(
                self.app_state.display_name
            )
        except Exception:
            display_name = ""

        if not display_name:
            display_name = "دانش‌آموز"

        self._info_card(
            "نام دانش‌آموز",
            display_name
        )

        self._action_row([
            (
                "برنامه هفتگی",
                lambda *_:
                self.show_module("schedule")
            ),
            (
                "وضعیت تحصیلی",
                lambda *_:
                self.show_module("student_info")
            ),
        ])

        self._action_row([
            (
                "کلاس آنلاین",
                lambda *_:
                self.show_module("online")
            ),
            (
                "پیام‌ها",
                lambda *_:
                self.show_module("messages")
            ),
        ])

        self._action_row([
            (
                "درباره فراهوش",
                lambda *_:
                self.show_module("about")
            ),
        ])


    # =====================================================
    # STUDENTS
    # =====================================================

    def _students(self):

        self._section_title(
            "دانش‌آموزان"
        )

        self._set_status(
            "در حال دریافت اطلاعات دانش‌آموزان..."
        )

        self._load_table(
            ["students", "student_records"],
            "دانش‌آموزان"
        )


    # =====================================================
    # PARENT PANEL
    # =====================================================

    def _parent(self):

        self._section_title(
            "پنل اولیا"
        )

        display_name = ""

        try:
            display_name = safe_str(
                self.app_state.display_name
            )
        except Exception:
            display_name = ""

        if not display_name:
            display_name = "ولی دانش‌آموز"

        self._info_card(
            "کاربر",
            display_name
        )

        self._action_row([
            (
                "وضعیت تحصیلی",
                lambda *_:
                self.show_module("student_info")
            ),
            (
                "پرداخت‌ها",
                lambda *_:
                self.show_module("payment")
            ),
        ])

        self._action_row([
            (
                "کلاس آنلاین",
                lambda *_:
                self.show_module("online")
            ),
            (
                "پیام‌ها",
                lambda *_:
                self.show_module("messages")
            ),
        ])


    # =====================================================
    # PARENTS
    # =====================================================

    def _parents(self):

        self._section_title(
            "اولیا"
        )

        self._set_status(
            "در حال دریافت اطلاعات اولیا..."
        )

        self._load_table(
            ["parents", "parent_records"],
            "اولیا"
        )


    # =====================================================
    # TABLE LOADER
    # =====================================================

    def _load_table(
        self,
        table_names,
        title="اطلاعات"
    ):

        if isinstance(
            table_names,
            str
        ):
            table_names = [
                table_names
            ]


        self.content.add_widget(

            make_label(
                "لطفاً چند لحظه صبر کنید...",
                font_size="14sp",
                color=SECONDARY,
                height=dp(50),
            )
        )


        api = None

        try:
            api = self.app_state.api
        except Exception:
            api = None


        if api is None:

            self._set_status(
                "اتصال سرویس اطلاعاتی برقرار نیست.",
                ERROR
            )

            self._placeholder(
                "اطلاعات این بخش در حال حاضر قابل دریافت نیست."
            )

            return


        # -------------------------------------------------
        # Try tables one by one.
        # -------------------------------------------------

        rows = None
        used_table = None
        last_error = None


        for table_name in table_names:

            try:

                result = api.table_select(
                    table_name
                )

                if result is not None:

                    rows = result

                    used_table = table_name

                    break

            except Exception as exc:

                last_error = exc


        # -------------------------------------------------
        # Remove loading widgets.
        # -------------------------------------------------

        self.content.clear_widgets()


        self._section_title(
            title
        )


        if rows is None:

            message = (
                "امکان دریافت اطلاعات وجود ندارد."
            )

            if last_error:

                print(
                    "TABLE LOAD ERROR:",
                    repr(last_error)
                )

                message = (
                    "اتصال به سرور یا جدول اطلاعاتی "
                    "با مشکل مواجه شد."
                )


            self._set_status(
                message,
                ERROR
            )

            self._placeholder(
                "در صورت اتصال صحیح سرور، "
                "اطلاعات این بخش نمایش داده می‌شود."
            )

            return


        if not isinstance(
            rows,
            list
        ):

            rows = []


        if not rows:

            self._set_status(
                "اطلاعاتی برای نمایش ثبت نشده است.",
                SECONDARY
            )

            self._placeholder(
                "در حال حاضر رکوردی در این بخش وجود ندارد."
            )

            return


        self._set_status(
            f"{len(rows)} رکورد دریافت شد.",
            SUCCESS
        )


        # -------------------------------------------------
        # Determine columns.
        # -------------------------------------------------

        columns = []

        for row in rows:

            if not isinstance(
                row,
                dict
            ):
                continue

            for key in row.keys():

                if key not in columns:

                    columns.append(
                        key
                    )


        if not columns:

            self._placeholder(
                "ساختار اطلاعات قابل نمایش نیست."
            )

            return


        # -------------------------------------------------
        # Header.
        # -------------------------------------------------

        header = GridLayout(
            cols=1,
            spacing=dp(4),
            size_hint_y=None,
            height=dp(44),
        )

        header.add_widget(

            make_label(
                " | ".join(
                    safe_str(x)
                    for x in columns
                ),
                font_size="12sp",
                color=PRIMARY,
                bold=True,
                height=dp(42),
            )
        )

        self.content.add_widget(
            header
        )


        # -------------------------------------------------
        # Rows.
        # -------------------------------------------------

        for index, row in enumerate(rows):

            if not isinstance(
                row,
                dict
            ):
                continue


            values = []

            for column in columns:

                values.append(
                    safe_str(
                        row.get(
                            column,
                            ""
                        )
                    )
                )


            text = " | ".join(
                values
            )


            self.content.add_widget(

                make_label(
                    text,
                    font_size="12sp",
                    color=SECONDARY,
                    height=dp(58),
                )
            )


        if used_table:

            print(
                "TABLE LOADED:",
                used_table
            )

    # =====================================================
    # FINANCE
    # =====================================================

    def _finance(self):

        self._section_title(
            "امور مالی"
        )

        self._info_card(
            "مدیریت مالی",
            "ثبت و مشاهده پرداخت‌های دانش‌آموزان"
        )

        self._action_row([
            (
                "پرداخت‌ها",
                lambda *_:
                self.show_module("payment")
            ),
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
        ])

        self._set_status(
            "در حال دریافت سوابق مالی..."
        )

        self._load_table(
            [
                "payment_records",
                "financial_records",
            ],
            "سوابق مالی"
        )


    # =====================================================
    # PAYMENT
    # =====================================================

    def _payment(self):

        self._section_title(
            "پرداخت‌ها"
        )

        self._info_card(
            "وضعیت پرداخت",
            "سوابق پرداخت دانش‌آموزان"
        )

        self._action_row([
            (
                "بازگشت به مالی",
                lambda *_:
                self.show_module("finance")
            ),
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
        ])

        self._set_status(
            "در حال دریافت سوابق پرداخت..."
        )

        self._load_table(
            [
                "payment_records"
            ],
            "سوابق پرداخت"
        )


    # =====================================================
    # ONLINE CLASSES
    # =====================================================

    def _online(self):

        self._section_title(
            "کلاس‌های آنلاین"
        )

        self._info_card(
            "کلاس آنلاین",
            "مدیریت کلاس‌های فعال و دسترسی دانش‌آموزان و دبیران"
        )

        self._action_row([
            (
                "کلاس‌های فعال",
                lambda *_:
                self._refresh_current()
            ),
            (
                "پیام‌ها",
                lambda *_:
                self.show_module("messages")
            ),
        ])

        self._set_status(
            "در حال دریافت کلاس‌های آنلاین..."
        )

        self._load_table(
            [
                "online_classes",
                "classes",
            ],
            "کلاس‌های آنلاین"
        )


    # =====================================================
    # SMART BOARD
    # =====================================================

    def _smart_board(self):

        self._section_title(
            "تابلو هوشمند"
        )

        self._info_card(
            "تابلو هوشمند",
            "محتوای آموزشی، فایل‌ها، تصاویر، ویدئوها و فعالیت‌های کوتاه"
        )

        self._action_row([
            (
                "محتوا",
                lambda *_:
                self._refresh_current()
            ),
            (
                "کلاس آنلاین",
                lambda *_:
                self.show_module("online")
            ),
        ])

        self._set_status(
            "در حال دریافت محتوای تابلو..."
        )

        self._load_table(
            [
                "smart_board_content",
                "smart_board",
            ],
            "محتوای تابلو هوشمند"
        )


    # =====================================================
    # AI
    # =====================================================

    def _ai(self):

        self._section_title(
            "هوش مصنوعی"
        )

        self._info_card(
            "دستیار هوشمند",
            "ابزارهای هوشمند فراهوش برای تحلیل و گزارش آموزشی"
        )

        self._action_row([
            (
                "دستیار هوشمند",
                lambda *_:
                self._ai_assistant()
            ),
            (
                "تحلیل آموزشی",
                lambda *_:
                self._ai_analysis()
            ),
        ])

        self._action_row([
            (
                "گزارش هوشمند",
                lambda *_:
                self._ai_report()
            ),
            (
                "پرسش و پاسخ",
                lambda *_:
                self._ai_questions()
            ),
        ])

        self._section_title(
            "سوابق درخواست‌های هوشمند"
        )

        self._set_status(
            "در حال دریافت سوابق..."
        )

        self._load_table(
            [
                "ai_requests",
                "ai_analysis",
                "ai_reports",
            ],
            "درخواست‌های هوش مصنوعی"
        )


    def _ai_assistant(self):

        self.content.clear_widgets()

        self._section_title(
            "دستیار هوشمند"
        )

        self._placeholder(
            "دستیار هوشمند آماده دریافت درخواست شماست."
        )

        self._ai_input(
            "درخواست خود را وارد کنید..."
        )


    def _ai_analysis(self):

        self.content.clear_widgets()

        self._section_title(
            "تحلیل آموزشی"
        )

        self._placeholder(
            "در این بخش می‌توان وضعیت آموزشی و عملکرد دانش‌آموزان را تحلیل کرد."
        )

        self._ai_input(
            "موضوع تحلیل را وارد کنید..."
        )


    def _ai_report(self):

        self.content.clear_widgets()

        self._section_title(
            "گزارش هوشمند"
        )

        self._placeholder(
            "گزارش هوشمند بر اساس اطلاعات ثبت‌شده مدرسه تولید خواهد شد."
        )

        self._ai_input(
            "موضوع گزارش را وارد کنید..."
        )


    def _ai_questions(self):

        self.content.clear_widgets()

        self._section_title(
            "پرسش و پاسخ"
        )

        self._placeholder(
            "سؤال خود را برای دستیار هوشمند وارد کنید."
        )

        self._ai_input(
            "سؤال خود را بنویسید..."
        )


    def _ai_input(self, hint):

        box = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            size_hint_y=None,
            height=dp(150),
        )

        field = TextInput(
            hint_text=rtl_text(hint),
            font_name=font_name(),
            font_size="14sp",
            multiline=True,
            halign="right",
            size_hint_y=None,
            height=dp(90),
            background_normal="",
            background_color=(
                0.95,
                0.97,
                0.99,
                1,
            ),
            foreground_color=SECONDARY,
        )

        box.add_widget(field)

        box.add_widget(
            make_button(
                "ارسال درخواست",
                lambda *_:
                self._submit_ai_request(
                    field.text
                ),
                height=dp(48),
            )
        )

        self.content.add_widget(box)


    def _submit_ai_request(self, text):

        text = safe_str(text).strip()

        if not text:

            self._set_status(
                "ابتدا درخواست یا سؤال خود را وارد کنید.",
                ERROR,
            )

            return

        self._set_status(
            "درخواست ثبت شد. اتصال سرویس هوش مصنوعی در حال بررسی است.",
            SUCCESS,
        )

        print(
            "AI REQUEST:",
            text
        )


    # =====================================================
    # REPORTS
    # =====================================================

    def _reports(self):

        self._section_title(
            "گزارش‌ها"
        )

        self._info_card(
            "گزارش‌های مدرسه",
            "مشاهده گزارش‌های آموزشی و اجرایی"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "دبیران",
                lambda *_:
                self.show_module("teachers")
            ),
        ])

        self._set_status(
            "در حال دریافت گزارش‌ها..."
        )

        self._load_table(
            [
                "reports",
                "report_cards",
            ],
            "گزارش‌ها"
        )


    # =====================================================
    # MESSAGES
    # =====================================================

    def _messages(self):

        self._section_title(
            "پیام‌ها"
        )

        self._info_card(
            "پیام‌رسانی",
            "پیام‌های مدرسه و اطلاع‌رسانی"
        )

        self._action_row([
            (
                "پیام‌های دریافتی",
                lambda *_:
                self._refresh_current()
            ),
            (
                "اولیا",
                lambda *_:
                self.show_module("parents")
            ),
        ])

        self._set_status(
            "در حال دریافت پیام‌ها..."
        )

        self._load_table(
            [
                "messages",
                "message_records",
            ],
            "پیام‌ها"
        )


    # =====================================================
    # SETTINGS
    # =====================================================

    def _settings(self):

        self._section_title(
            "تنظیمات"
        )

        self._info_card(
            "اطلاعات مدرسه",
            SCHOOL_NAME
        )

        self._action_row([
            (
                "اطلاعات مدرسه",
                lambda *_:
                self._school_settings()
            ),
            (
                "حساب‌های کاربران",
                lambda *_:
                self._account_settings()
            ),
        ])

        self._section_title(
            "تنظیمات سامانه"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "دبیران",
                lambda *_:
                self.show_module("teachers")
            ),
        ])


        self._set_status(
            "تنظیمات آماده استفاده است.",
            SUCCESS
        )


    def _school_settings(self):

        self.content.clear_widgets()

        self._section_title(
            "اطلاعات مدرسه"
        )

        self._info_card(
            "نام مدرسه",
            SCHOOL_NAME
        )

        self._info_card(
            "سامانه",
            APP_NAME
        )

        self._placeholder(
            "اطلاعات مدرسه از تنظیمات سامانه خوانده می‌شود."
        )

        self._action_row([
            (
                "بازگشت",
                lambda *_:
                self.show_module("settings")
            ),
        ])


    def _account_settings(self):

        self.content.clear_widgets()

        self._section_title(
            "حساب‌های کاربران"
        )

        self._set_status(
            "در حال دریافت حساب‌ها..."
        )

        self._load_table(
            [
                "account_settings"
            ],
            "حساب‌های کاربران"
        )


    # =====================================================
    # WEEKLY SCHEDULE
    # =====================================================

    def _schedule(self):

        self._section_title(
            "برنامه هفتگی"
        )

        self._info_card(
            "برنامه مدرسه",
            "برنامه هفتگی کلاس‌ها و دبیران"
        )

        self._placeholder(
            "برنامه هفتگی پس از اتصال جدول برنامه مدرسه نمایش داده می‌شود."
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "دبیران",
                lambda *_:
                self.show_module("teachers")
            ),
        ])


    # =====================================================
    # STUDENT INFORMATION
    # =====================================================

    def _student_info(self):

        self._section_title(
            "وضعیت تحصیلی"
        )

        self._info_card(
            "وضعیت دانش‌آموز",
            "نمرات، ارزیابی و وضعیت آموزشی"
        )

        self._action_row([
            (
                "دانش‌آموزان",
                lambda *_:
                self.show_module("students")
            ),
            (
                "گزارش‌ها",
                lambda *_:
                self.show_module("reports")
            ),
        ])

        self._set_status(
            "در حال دریافت اطلاعات تحصیلی..."
        )

        self._load_table(
            [
                "student_records",
                "students",
            ],
            "اطلاعات تحصیلی"
        )


    # =====================================================
    # ABOUT
    # =====================================================

    def _about(self):

        self._section_title(
            "درباره فراهوش"
        )

        self._info_card(
            "نام سامانه",
            APP_NAME
        )

        self._info_card(
            "مدرسه",
            SCHOOL_NAME
        )

        self._info_card(
            "نسخه",
            "1.1.1"
        )

        self._placeholder(
            "فراهوش؛ سامانه هوشمند آموزشی یکپارچه مدرسه."
        )

        self._action_row([
            (
                "بازگشت به داشبورد",
                self._go_back,
            ),
        ])


    # =====================================================
    # CURRENT MODULE REFRESH
    # =====================================================

    def _refresh_current(self, *_args):

        if self.module_key:

            return self.show_module(
                self.module_key
            )

        return False


    # =====================================================
    # ERROR HELPER
    # =====================================================

    def _show_error(self, message):

        self._set_status(
            message,
            ERROR,
        )

        self.content.add_widget(
            make_label(
                message,
                font_size="14sp",
                color=ERROR,
                height=dp(70),
            )
        )


    # =====================================================
    # TEXT SIZE SUPPORT
    # =====================================================

    def _sync_text_size(
        self,
        widget,
        size
    ):

        try:

            widget.text_size = (
                size[0],
                None
            )

        except Exception:

            pass



