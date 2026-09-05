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
    "executive": "معاون اجرایی",
    "vice": "معاون",
    "vice_principal": "معاون",
    "educational": "معاون آموزشی",
    "cultural": "معاون پرورشی",
    "advisor": "مشاور",
    "counselor": "مشاور",
    "teacher": "دبیر",
    "student": "دانش‌آموز",
    "parent": "ولی",
}


ROLE_MODULES = {

    "manager": [
        ("مدیریت مدرسه", "school"),
        ("دانش‌آموزان", "students"),
        ("دبیران", "teachers"),
        ("کارکنان", "staff"),
        ("کلاس‌ها", "classes"),
        ("برنامه هفتگی", "schedule"),
        ("امتحانات", "exams"),
        ("کارت ورود به جلسه", "exam_cards"),
        ("گزارش نمرات", "grades"),
        ("کارنامه", "report_cards"),
        ("حضور و غیاب", "attendance"),
        ("انضباط", "discipline"),
        ("مشاوره", "counseling"),
        ("معاونت‌ها", "vice_principal"),
        ("اولیا", "parents"),
        ("پیام‌ها", "messages"),
        ("اعلان‌ها", "notifications"),
        ("صندوق پیشنهادات", "suggestions"),
        ("کلاس آنلاین", "online_classes"),
        ("آزمون آنلاین", "online_exams"),
        ("بانک سوالات", "question_bank"),
        ("تابلو هوشمند", "smart_board"),
        ("هوش مصنوعی", "ai"),
        ("مالی", "finance"),
        ("پرداخت‌ها", "payments"),
        ("انبار و اموال", "inventory"),
        ("گزارش‌ها", "reports"),
        ("تنظیمات", "settings"),
        ("کاربران و حساب‌ها", "users"),
    ],

    "admin": [
        ("مدیریت مدرسه", "school"),
        ("دانش‌آموزان", "students"),
        ("دبیران", "teachers"),
        ("کلاس‌ها", "classes"),
        ("امتحانات", "exams"),
        ("گزارش‌ها", "reports"),
        ("کلاس آنلاین", "online_classes"),
        ("هوش مصنوعی", "ai"),
        ("مالی", "finance"),
        ("پیام‌ها", "messages"),
        ("تنظیمات", "settings"),
    ],

    "teacher": [
        ("کلاس‌های من", "classes"),
        ("دانش‌آموزان", "students"),
        ("حضور و غیاب", "attendance"),
        ("نمرات", "grades"),
        ("انضباط", "discipline"),
        ("طرح درس", "lesson_plan"),
        ("تکالیف", "assignments"),
        ("بانک سوالات", "question_bank"),
        ("تقویم", "calendar"),
        ("امتحانات", "exams"),
        ("جلسات اولیا", "parent_meetings"),
        ("کلاس آنلاین", "online_classes"),
        ("آزمون آنلاین", "online_exams"),
        ("گزارش‌ها", "reports"),
        ("ارجاع دانش‌آموز", "referrals"),
        ("پیام‌ها", "messages"),
        ("هوش مصنوعی", "ai"),
        ("پروفایل", "profile"),
    ],

    "student": [
        ("پروفایل من", "profile"),
        ("کلاس من", "classes"),
        ("برنامه هفتگی", "schedule"),
        ("حضور و غیاب", "attendance"),
        ("نمرات", "grades"),
        ("کارنامه", "report_cards"),
        ("تکالیف", "assignments"),
        ("امتحانات", "exams"),
        ("کارت ورود به جلسه", "exam_cards"),
        ("کلاس آنلاین", "online_classes"),
        ("آزمون آنلاین", "online_exams"),
        ("پیام‌ها", "messages"),
        ("مسابقات فرهنگی", "cultural_competitions"),
        ("خوارزمی", "khwarizmi"),
        ("ورزش مدرسه", "sports"),
    ],

    "parent": [
        ("پروفایل فرزند", "child_profile"),
        ("وضعیت تحصیلی", "student_status"),
        ("گزارش ماهانه", "monthly_report"),
        ("حضور و غیاب", "attendance"),
        ("نمرات", "grades"),
        ("کارنامه", "report_cards"),
        ("تحلیل دانش‌آموز", "student_analysis"),
        ("پرداخت‌ها", "payments"),
        ("جلسه با دبیر", "teacher_meeting"),
        ("پیام‌های مدرسه", "school_messages"),
        ("وضعیت آنلاین", "live_status"),
        ("پیشنهادات", "suggestions"),
    ],

    "advisor": [
        ("داشبورد مشاوره", "counseling"),
        ("پرونده مشاوره", "counseling_file"),
        ("پیگیری دانش‌آموزان", "student_followup"),
        ("ارتباط با خانواده", "parent_contact"),
        ("ارجاعات", "referrals"),
        ("گزارش‌ها", "reports"),
        ("هدایت تحصیلی", "smart_guidance"),
    ],

    "counselor": [
        ("داشبورد مشاوره", "counseling"),
        ("پرونده مشاوره", "counseling_file"),
        ("پیگیری دانش‌آموزان", "student_followup"),
        ("گزارش‌ها", "reports"),
        ("ارجاعات", "referrals"),
    ],

    "executive": [
        ("داشبورد اجرایی", "executive"),
        ("دانش‌آموزان", "students"),
        ("کارکنان", "staff"),
        ("کلاس‌ها", "classes"),
        ("ثبت‌نام", "registration"),
        ("کارت دانش‌آموزی", "student_cards"),
        ("کارت امتحان", "exam_cards"),
        ("صندلی امتحان", "exam_seats"),
        ("گزارش‌ها", "reports"),
        ("بایگانی", "archive"),
        ("اموال", "inventory"),
        ("درخواست‌ها", "requests"),
        ("تنظیمات", "settings"),
    ],

    "vice": [
        ("داشبورد معاونت", "vice_principal"),
        ("انضباط", "discipline"),
        ("بررسی نمرات", "grades"),
        ("طرح درس‌ها", "lesson_plan"),
        ("ارجاعات", "referrals"),
        ("درخواست جلسات", "meetings"),
        ("گزارش‌ها", "reports"),
    ],

    "vice_principal": [
        ("داشبورد معاونت", "vice_principal"),
        ("انضباط", "discipline"),
        ("بررسی نمرات", "grades"),
        ("طرح درس‌ها", "lesson_plan"),
        ("ارجاعات", "referrals"),
        ("درخواست جلسات", "meetings"),
        ("گزارش‌ها", "reports"),
    ],

    "educational": [
        ("داشبورد آموزشی", "education"),
        ("ارزیابی‌ها", "evaluations"),
        ("امتحانات", "exams"),
        ("فعالیت‌های فوق برنامه", "extracurricular"),
        ("خوارزمی", "khwarizmi"),
        ("بانک سوالات", "question_bank"),
        ("ارجاعات", "referrals"),
        ("گزارش‌ها", "reports"),
    ],

    "cultural": [
        ("داشبورد پرورشی", "cultural"),
        ("مراسم‌ها", "ceremonies"),
        ("مسابقات", "competitions"),
        ("جشنواره‌ها", "festivals"),
        ("قرآن", "quran"),
        ("استعدادها", "talents"),
        ("اردوها", "trips"),
        ("گزارش‌ها", "reports"),
    ],
}


class DashboardScreen(Screen):

    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)

        self.app_state = app_state

        root = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(8)
        )

        self.header = Label(
            font_name=font_name(),
            font_size="20sp",
            color=PRIMARY,
            size_hint_y=None,
            height=dp(80)
        )

        root.add_widget(self.header)

        scroll = ScrollView()

        self.grid = GridLayout(
            cols=2,
            spacing=dp(8),
            padding=dp(4),
            size_hint_y=None
        )

        self.grid.bind(
            minimum_height=self.grid.setter("height")
        )

        scroll.add_widget(self.grid)
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

        role = self.app_state.role
        name = self.app_state.display_name

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

        for title, key in modules:

            btn = Button(
                text=rtl_text(title),
                font_name=font_name(),
                background_normal="",
                background_color=SECONDARY,
                color=WHITE,
                size_hint_y=None,
                height=dp(54)
            )

            btn.bind(
                on_release=lambda x, t=title, k=key:
                self.open_module(t, k)
            )

            self.grid.add_widget(btn)

        update = Button(
            text=rtl_text("مرکز به‌روزرسانی"),
            font_name=font_name(),
            background_normal="",
            background_color=SUCCESS,
            color=WHITE,
            size_hint_y=None,
            height=dp(54)
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
            color=WHITE,
            size_hint_y=None,
            height=dp(54)
        )

        logout.bind(
            on_release=self.logout
        )

        self.grid.add_widget(logout)

    def open_module(self, title, key):

        if not self.manager.has_screen("module"):

            from mobile.screens.module import ModuleScreen

            self.manager.add_widget(
                ModuleScreen(
                    self.app_state,
                    name="module"
                )
            )

        screen = self.manager.get_screen("module")

        screen.show_module(
            title,
            key,
            self.app_state.role
        )

        self.manager.current = "module"

    def open_update(self, *_):

        if self.manager.has_screen("update"):
            self.manager.current = "update"

    def logout(self, *_):

        if self.app_state:
            self.app_state.logout()

        self.manager.current = "login"
