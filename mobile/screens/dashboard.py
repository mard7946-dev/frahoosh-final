from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

from mobile.config import (
    APP_NAME,
    SCHOOL_NAME,
    APP_VERSION,
    PRIMARY,
    SECONDARY,
    WHITE,
)

from mobile.ui import font_name, rtl_text


# =========================================================
# ROLE TITLES
# =========================================================

ROLE_TITLES = {
    "manager": "مدیریت مدرسه",
    "admin": "مدیریت مدرسه",
    "principal": "مدیریت مدرسه",

    "educational": "معاون آموزشی",
    "education": "معاون آموزشی",
    "assistant_education": "معاون آموزشی",

    "executive": "معاون اجرایی",
    "assistant_executive": "معاون اجرایی",

    "cultural": "معاون پرورشی",
    "assistant_cultural": "معاون پرورشی",
    "training": "معاون پرورشی",

    "advisor": "مشاوره",
    "counselor": "مشاوره",

    "teacher": "دبیر",
    "teachers": "دبیران",

    "student": "دانش‌آموز",
    "students": "دانش‌آموزان",

    "parent": "ولی دانش‌آموز",
    "parents": "اولیا",
}


# =========================================================
# ROLE MENUS
# =========================================================

ROLE_MENUS = {

    "manager": [
        ("🏫 مدیریت مدرسه", "management"),
        ("📚 معاون آموزشی", "educational"),
        ("🗂 معاون اجرایی", "executive"),
        ("🎯 معاون پرورشی", "cultural"),
        ("👥 دبیران", "teachers"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("👨‍👩‍👦 اولیا", "parents"),
        ("💰 امور مالی", "finance"),
        ("💻 کلاس‌های آنلاین", "online"),
        ("🖥 تابلو هوشمند", "smart_board"),
        ("🤖 هوش مصنوعی", "ai"),
        ("📊 گزارش‌ها", "reports"),
        ("💬 پیام‌ها", "messages"),
        ("⚙️ تنظیمات", "settings"),
        ("📅 برنامه هفتگی", "schedule"),
        ("ℹ️ درباره فراهوش", "about"),
    ],

    "admin": [
        ("🏫 مدیریت مدرسه", "management"),
        ("👥 دبیران", "teachers"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("👨‍👩‍👦 اولیا", "parents"),
        ("💰 امور مالی", "finance"),
        ("💻 کلاس‌های آنلاین", "online"),
        ("🖥 تابلو هوشمند", "smart_board"),
        ("🤖 هوش مصنوعی", "ai"),
        ("📊 گزارش‌ها", "reports"),
        ("⚙️ تنظیمات", "settings"),
    ],

    "educational": [
        ("📚 معاون آموزشی", "educational"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("👥 دبیران", "teachers"),
        ("📅 برنامه هفتگی", "schedule"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("📈 گزارش‌ها", "reports"),
        ("💻 کلاس‌های آنلاین", "online"),
    ],

    "education": [
        ("📚 معاون آموزشی", "educational"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("👥 دبیران", "teachers"),
        ("📅 برنامه هفتگی", "schedule"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("📈 گزارش‌ها", "reports"),
    ],

    "executive": [
        ("🗂 معاون اجرایی", "executive"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("👨‍👩‍👦 اولیا", "parents"),
        ("💰 امور مالی", "finance"),
        ("📊 گزارش‌ها", "reports"),
        ("⚙️ تنظیمات", "settings"),
    ],

    "cultural": [
        ("🎯 معاون پرورشی", "cultural"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("🖥 تابلو هوشمند", "smart_board"),
        ("💬 پیام‌ها", "messages"),
        ("📊 گزارش‌ها", "reports"),
    ],

    "training": [
        ("🎯 معاون پرورشی", "cultural"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("🖥 تابلو هوشمند", "smart_board"),
        ("💬 پیام‌ها", "messages"),
    ],

    "advisor": [
        ("🧠 مشاوره", "advisor"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("📈 گزارش‌ها", "reports"),
        ("💬 پیام‌ها", "messages"),
    ],

    "counselor": [
        ("🧠 مشاوره", "advisor"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("📈 گزارش‌ها", "reports"),
    ],

    "teacher": [
        ("👨‍🏫 پنل دبیر", "teacher"),
        ("📅 برنامه هفتگی", "schedule"),
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("💻 کلاس‌های آنلاین", "online"),
        ("📊 گزارش‌ها", "reports"),
        ("💬 پیام‌ها", "messages"),
    ],

    "teachers": [
        ("👨‍🏫 دبیران", "teachers"),
        ("📅 برنامه هفتگی", "schedule"),
        ("💻 کلاس‌های آنلاین", "online"),
        ("💬 پیام‌ها", "messages"),
    ],

    "student": [
        ("👨‍🎓 پنل دانش‌آموز", "student"),
        ("📅 برنامه هفتگی", "schedule"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("💻 کلاس آنلاین", "online"),
        ("💬 پیام‌ها", "messages"),
    ],

    "students": [
        ("👨‍🎓 دانش‌آموزان", "students"),
        ("📅 برنامه هفتگی", "schedule"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("💻 کلاس آنلاین", "online"),
    ],

    "parent": [
        ("👨‍👩‍👦 پنل اولیا", "parent"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("💳 پرداخت‌ها", "payment"),
        ("💻 کلاس آنلاین", "online"),
        ("💬 پیام‌ها", "messages"),
    ],

    "parents": [
        ("👨‍👩‍👦 اولیا", "parents"),
        ("📊 وضعیت تحصیلی", "student_info"),
        ("💳 پرداخت‌ها", "payment"),
        ("💻 کلاس آنلاین", "online"),
        ("💬 پیام‌ها", "messages"),
    ],
}


# =========================================================
# DASHBOARD SCREEN
# =========================================================

class DashboardScreen(Screen):

    def __init__(self, app_state, **kwargs):

        super().__init__(**kwargs)

        self.app_state = app_state

        self.drawer_open = False

        self.drawer = None

        self.drawer_width = dp(285)

        self.content_area = None

        self.welcome_label = None

        self.role_label = None

        self._build_ui()


    # =====================================================
    # BUILD UI
    # =====================================================

    def _build_ui(self):

        self.clear_widgets()

        root = FloatLayout()


        # -------------------------------------------------
        # Background
        # -------------------------------------------------

        with root.canvas.before:

            Color(
                0.035,
                0.09,
                0.14,
                1,
            )

            self.background_rect = RoundedRectangle(
                pos=root.pos,
                size=root.size,
            )

        root.bind(
            pos=lambda obj, value:
            setattr(
                self.background_rect,
                "pos",
                value,
            ),

            size=lambda obj, value:
            setattr(
                self.background_rect,
                "size",
                value,
            ),
        )


        # -------------------------------------------------
        # Main container
        # -------------------------------------------------

        main = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=[
                dp(12),
                dp(12),
                dp(12),
                dp(12),
            ],
        )


        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(58),
            spacing=dp(8),
        )


        menu_button = Button(
            text="☰",
            font_size="28sp",
            font_name=font_name(),
            color=WHITE,
            background_normal="",
            background_color=(
                0.05,
                0.22,
                0.34,
                1,
            ),
            size_hint_x=None,
            width=dp(58),
        )

        menu_button.bind(
            on_release=self.toggle_drawer
        )

        header.add_widget(
            menu_button
        )


        title_box = BoxLayout(
            orientation="vertical",
        )


        title_box.add_widget(
            self._label(
                APP_NAME,
                "20sp",
                WHITE,
                True,
                dp(32),
            )
        )


        title_box.add_widget(
            self._label(
                "سامانه هوشمند آموزشی یکپارچه",
                "11sp",
                (
                    0.78,
                    0.86,
                    0.92,
                    1,
                ),
                False,
                dp(22),
            )
        )


        header.add_widget(
            title_box
        )


        main.add_widget(
            header
        )


        # -------------------------------------------------
        # Welcome card
        # -------------------------------------------------

        welcome = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(5),
            size_hint_y=None,
            height=dp(120),
        )


        with welcome.canvas.before:

            Color(
                1,
                1,
                1,
                0.96,
            )

            welcome_rect = RoundedRectangle(
                radius=[dp(18)],
            )


        welcome.bind(
            pos=lambda obj, value:
            setattr(
                welcome_rect,
                "pos",
                value,
            ),

            size=lambda obj, value:
            setattr(
                welcome_rect,
                "size",
                value,
            ),
        )


        self.welcome_label = self._label(
            "خوش آمدید",
            "20sp",
            PRIMARY,
            True,
            dp(42),
        )

        welcome.add_widget(
            self.welcome_label
        )


        self.role_label = self._label(
            "",
            "14sp",
            SECONDARY,
            False,
            dp(30),
        )

        welcome.add_widget(
            self.role_label
        )


        school_label = self._label(
            SCHOOL_NAME,
            "12sp",
            SECONDARY,
            False,
            dp(25),
        )

        welcome.add_widget(
            school_label
        )


        main.add_widget(
            welcome
        )


        # -------------------------------------------------
        # Content area
        # -------------------------------------------------

        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
        )


        self.content_area = BoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=[
                dp(4),
                dp(8),
                dp(4),
                dp(20),
            ],
            size_hint_y=None,
        )


        self.content_area.bind(
            minimum_height=
            self.content_area.setter(
                "height"
            )
        )


        scroll.add_widget(
            self.content_area
        )

        main.add_widget(
            scroll
        )


        # -------------------------------------------------
        # Version
        # -------------------------------------------------

        main.add_widget(
            self._label(
                f"نسخه {APP_VERSION}",
                "10sp",
                (
                    0.70,
                    0.78,
                    0.84,
                    1,
                ),
                False,
                dp(22),
            )
        )


        root.add_widget(
            main
        )


        # -------------------------------------------------
        # Drawer
        # -------------------------------------------------

        self.drawer = self._build_drawer()

        root.add_widget(
            self.drawer
        )


        self.add_widget(
            root
        )


    # =====================================================
    # LABEL HELPER
    # =====================================================

    def _label(
        self,
        text,
        font_size="14sp",
        color=WHITE,
        bold=False,
        height=dp(40),
    ):

        label = Label(
            text=rtl_text(
                str(text)
            ),
            font_name=font_name(),
            font_size=font_size,
            color=color,
            bold=bold,
            halign="right",
            valign="middle",
            size_hint_y=None,
            height=height,
        )

        label.bind(
            size=lambda obj, value:
            setattr(
                obj,
                "text_size",
                value,
            )
        )

        return label


    # =====================================================
    # DRAWER
    # =====================================================

    def _build_drawer(self):

        drawer = BoxLayout(
            orientation="vertical",
            size_hint_x=None,
            width=self.drawer_width,
            size_hint_y=1,
            pos_hint={
                "x": -1,
                "y": 0,
            },
            padding=[
                dp(14),
                dp(16),
                dp(14),
                dp(16),
            ],
            spacing=dp(8),
        )


        with drawer.canvas.before:

            Color(
                0.035,
                0.12,
                0.18,
                1,
            )

            drawer_rect = RoundedRectangle(
                radius=[dp(12)],
            )


        drawer.bind(
            pos=lambda obj, value:
            setattr(
                drawer_rect,
                "pos",
                value,
            ),

            size=lambda obj, value:
            setattr(
                drawer_rect,
                "size",
                value,
            ),
        )


        # -------------------------------------------------
        # Drawer header
        # -------------------------------------------------

        drawer.add_widget(
            self._label(
                APP_NAME,
                "22sp",
                WHITE,
                True,
                dp(44),
            )
        )


        drawer.add_widget(
            self._label(
                SCHOOL_NAME,
                "12sp",
                (
                    0.80,
                    0.88,
                    0.92,
                    1,
                ),
                False,
                dp(45),
            )
        )


        # -------------------------------------------------
        # Menu scroll
        # -------------------------------------------------

        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
        )


        menu_box = BoxLayout(
            orientation="vertical",
            spacing=dp(7),
            size_hint_y=None,
            padding=[
                0,
                dp(5),
                0,
                dp(15),
            ],
        )


        menu_box.bind(
            minimum_height=
            menu_box.setter(
                "height"
            )
        )


        self._populate_menu(
            menu_box
        )


        scroll.add_widget(
            menu_box
        )


        drawer.add_widget(
            scroll
        )


        # -------------------------------------------------
        # Close button
        # -------------------------------------------------

        close_button = Button(
            text=rtl_text(
                "بستن منو"
            ),
            font_name=font_name(),
            font_size="14sp",
            color=WHITE,
            background_normal="",
            background_color=(
                0.20,
                0.25,
                0.30,
                1,
            ),
            size_hint_y=None,
            height=dp(48),
        )

        close_button.bind(
            on_release=
            self.close_drawer
        )


        drawer.add_widget(
            close_button
        )


        return drawer


    # =====================================================
    # POPULATE MENU
    # =====================================================

    def _populate_menu(
        self,
        menu_box,
    ):

        role = self._get_role()

        items = ROLE_MENUS.get(
            role
        )


        if not items:

            items = ROLE_MENUS.get(
                "manager"
            )


        for title, route in items:

            button = Button(
                text=rtl_text(
                    title
                ),
                font_name=font_name(),
                font_size="13sp",
                color=WHITE,
                halign="right",
                valign="middle",
                background_normal="",
                background_color=(
                    0.07,
                    0.20,
                    0.28,
                    1,
                ),
                size_hint_y=None,
                height=dp(46),
            )


            button.bind(
                size=lambda obj, value:
                setattr(
                    obj,
                    "text_size",
                    value,
                )
            )


            button.bind(
                on_release=lambda btn,
                r=route:
                self._menu_selected(r)
            )


            menu_box.add_widget(
                button
            )

    # ---------------------------------------------------------
    # Role / User helpers
    # ---------------------------------------------------------

    def _get_role(self):
        """
        دریافت نقش کاربر به شکل امن.
        """
        try:
            role = getattr(self.app_state, "role", None)

            if callable(role):
                role = role()

            if role:
                return str(role).strip().lower()

        except Exception:
            pass

        return "manager"

    def _get_display_name(self):
        """
        دریافت نام نمایشی کاربر.
        """
        try:
            name = getattr(self.app_state, "display_name", None)

            if callable(name):
                name = name()

            if name:
                return str(name).strip()

        except Exception:
            pass

        try:
            profile = getattr(self.app_state, "profile", None)

            if isinstance(profile, dict):
                for key in (
                    "full_name",
                    "display_name",
                    "name",
                    "first_name",
                    "username",
                ):
                    value = profile.get(key)

                    if value:
                        return str(value).strip()

        except Exception:
            pass

        return "کاربر"

    # ---------------------------------------------------------
    # Drawer control
    # ---------------------------------------------------------

    def _open_drawer(self, *args):
        """
        باز کردن منوی کناری.
        """
        if not self.drawer:
            return

        self.drawer_open = True

        try:
            from kivy.animation import Animation

            target_x = 0

            Animation(
                x=target_x,
                duration=0.20,
                t="out_quad",
            ).start(self.drawer)

        except Exception:
            try:
                self.drawer.x = 0
            except Exception:
                pass

    def _close_drawer(self, *args):
        """
        بستن منوی کناری.
        """
        if not self.drawer:
            return

        self.drawer_open = False

        try:
            from kivy.animation import Animation

            Animation(
                x=-self.drawer_width,
                duration=0.20,
                t="out_quad",
            ).start(self.drawer)

        except Exception:
            try:
                self.drawer.x = -self.drawer_width
            except Exception:
                pass

    def _toggle_drawer(self, *args):
        """
        باز/بسته کردن منوی کناری.
        """
        if self.drawer_open:
            self._close_drawer()
        else:
            self._open_drawer()

    # ---------------------------------------------------------
    # Menu navigation
    # ---------------------------------------------------------

    def _menu_selected(self, route):
        """
        انتقال از داشبورد به ماژول انتخاب‌شده.
        """
        try:
            self._close_drawer()

            manager = self.manager

            if manager is None:
                return

            if not hasattr(manager, "has_screen"):
                return

            if not manager.has_screen("module"):
                return

            module_screen = manager.get_screen("module")

            if module_screen is None:
                return

            if hasattr(module_screen, "set_module"):
                module_screen.set_module(route)

            elif hasattr(module_screen, "load_module"):
                module_screen.load_module(route)

            manager.current = "module"

        except Exception as exc:
            print("Dashboard navigation error:", exc)

            try:
                self._show_navigation_error(str(exc))
            except Exception:
                pass

    def _show_navigation_error(self, message):
        """
        نمایش خطای ناوبری بدون کرش برنامه.
        """
        try:
            if self.content_area is None:
                return

            self.content_area.clear_widgets()

            box = BoxLayout(
                orientation="vertical",
                spacing=dp(12),
                padding=dp(20),
                size_hint_y=None,
            )

            box.bind(
                minimum_height=box.setter("height")
            )

            title = self._label(
                "خطا در باز کردن بخش",
                font_size=20,
                bold=True,
                size_hint_y=None,
                height=dp(45),
            )

            detail = self._label(
                "لطفاً دوباره تلاش کنید.",
                font_size=15,
                size_hint_y=None,
                height=dp(70),
            )

            box.add_widget(title)
            box.add_widget(detail)

            self.content_area.add_widget(box)

        except Exception as exc:
            print("Navigation error display failed:", exc)

    # ---------------------------------------------------------
    # Dashboard content
    # ---------------------------------------------------------

    def _update_welcome(self):
        """
        به‌روزرسانی متن خوش‌آمدگویی و نقش کاربر.
        """
        name = self._get_display_name()
        role = self._get_role()

        role_title = ROLE_TITLES.get(
            role,
            "کاربر سامانه",
        )

        if self.welcome_label:
            try:
                self.welcome_label.text = (
                    f"خوش آمدید {name} عزیز"
                )
            except Exception:
                pass

        if self.role_label:
            try:
                self.role_label.text = role_title
            except Exception:
                pass

    def _show_dashboard_home(self):
        """
        نمایش صفحه اصلی داشبورد.
        """
        if self.content_area is None:
            return

        try:
            self.content_area.clear_widgets()

            box = BoxLayout(
                orientation="vertical",
                spacing=dp(12),
                padding=dp(16),
                size_hint_y=None,
            )

            box.bind(
                minimum_height=box.setter("height")
            )

            welcome = self._label(
                "به سامانه هوشمند آموزشی یکپارچه فراهوش خوش آمدید",
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=dp(65),
            )

            welcome.halign = "right"
            welcome.valign = "middle"

            info = self._label(
                "از منوی کناری، بخش مورد نظر خود را انتخاب کنید.",
                font_size=15,
                size_hint_y=None,
                height=dp(55),
            )

            info.halign = "right"
            info.valign = "middle"

            box.add_widget(welcome)
            box.add_widget(info)

            self.content_area.add_widget(box)

        except Exception as exc:
            print("Dashboard home error:", exc)

    # ---------------------------------------------------------
    # Refresh
    # ---------------------------------------------------------

    def refresh(self):
        """
        تازه‌سازی کامل داشبورد پس از ورود.
        """
        try:
            self._update_welcome()

            if self.drawer is not None:
                self._refresh_menu()

            self._show_dashboard_home()

        except Exception as exc:
            print("Dashboard refresh error:", exc)

    def _refresh_menu(self):
        """
        بازسازی منوی کناری براساس نقش فعلی.
        """
        try:
            if self.drawer is None:
                return

            scroll = None

            for child in self.drawer.children:
                if isinstance(child, ScrollView):
                    scroll = child
                    break

            if scroll is None:
                return

            menu_box = scroll.children[0] if scroll.children else None

            if menu_box is None:
                return

            menu_box.clear_widgets()
            self._populate_menu(menu_box)

        except Exception as exc:
            print("Drawer refresh error:", exc)

    # ---------------------------------------------------------
    # Screen lifecycle
    # ---------------------------------------------------------

    def on_enter(self, *args):
        """
        هنگام ورود به داشبورد.
        """
        try:
            self._update_welcome()

            if self.drawer is not None:
                try:
                    self.drawer.x = -self.drawer_width
                except Exception:
                    pass

            self.drawer_open = False

            Clock.schedule_once(
                lambda dt: self.refresh(),
                0,
            )

        except Exception as exc:
            print("Dashboard on_enter error:", exc)

    def on_leave(self, *args):
        """
        هنگام خروج از داشبورد.
        """
        try:
            self._close_drawer()
        except Exception:
            pass

    # ---------------------------------------------------------
    # Logout
    # ---------------------------------------------------------

    def _logout(self, *args):
        """
        خروج امن از حساب کاربری.
        """
        try:
            self._close_drawer()

            try:
                if hasattr(self.app_state, "logout"):
                    self.app_state.logout()
                elif hasattr(self.app_state, "api"):
                    api = self.app_state.api

                    if hasattr(api, "sign_out"):
                        api.sign_out()

            except Exception as exc:
                print("Logout backend error:", exc)

            manager = self.manager

            if manager is not None and manager.has_screen("login"):
                manager.current = "login"

        except Exception as exc:
            print("Dashboard logout error:", exc)

    # ---------------------------------------------------------
    # Safe button helper
    # ---------------------------------------------------------

    def _safe_bind(self, widget, event, callback):
        """
        اتصال امن callback به ویجت.
        """
        try:
            widget.bind(**{event: callback})
        except Exception as exc:
            print("Bind error:", exc)

    # ---------------------------------------------------------
    # Prevent accidental drawer interaction
    # ---------------------------------------------------------

    def on_touch_down(self, touch):
        """
        مدیریت لمس برای باز و بسته شدن منوی کناری.
        """
        try:
            if self.drawer_open and self.drawer:

                drawer_right = self.drawer.x + self.drawer.width

                # اگر بیرون از منوی کناری لمس شد
                if touch.x > drawer_right:
                    self._close_drawer()
                    return True

        except Exception:
            pass

        return super().on_touch_down(touch)

    # ---------------------------------------------------------
    # Utility / UI helpers
    # ---------------------------------------------------------

    def _label(
        self,
        text="",
        font_size=16,
        bold=False,
        **kwargs,
    ):
        """
        ساخت Label با تنظیمات مناسب فارسی.
        """
        try:
            label = Label(
                text=str(text),
                font_name=font_name(bold=bold),
                font_size=font_size,
                color=WHITE,
                **kwargs,
            )

            label.halign = "right"
            label.valign = "middle"

            try:
                label.text_size = (
                    label.width if label.width else None,
                    None,
                )
            except Exception:
                pass

            return label

        except Exception:
            return Label(
                text=str(text),
                font_size=font_size,
                color=WHITE,
                **kwargs,
            )

    def _show_loading(self):
        """
        نمایش وضعیت بارگذاری.
        """
        try:
            if self.content_area is None:
                return

            self.content_area.clear_widgets()

            loading = self._label(
                "در حال بارگذاری...",
                font_size=18,
                size_hint_y=None,
                height=dp(60),
            )

            self.content_area.add_widget(loading)

        except Exception as exc:
            print("Dashboard loading error:", exc)

    def _show_message(self, message):
        """
        نمایش پیام ساده در داشبورد.
        """
        try:
            if self.content_area is None:
                return

            self.content_area.clear_widgets()

            box = BoxLayout(
                orientation="vertical",
                padding=dp(20),
                spacing=dp(12),
                size_hint_y=None,
            )

            box.bind(
                minimum_height=box.setter("height")
            )

            label = self._label(
                message,
                font_size=16,
                size_hint_y=None,
                height=dp(100),
            )

            box.add_widget(label)
            self.content_area.add_widget(box)

        except Exception as exc:
            print("Dashboard message error:", exc)

    # ---------------------------------------------------------
    # Back handling
    # ---------------------------------------------------------

    def go_back(self, *args):
        """
        بازگشت به داشبورد اصلی.
        """
        try:
            self._close_drawer()

            if self.manager:
                self.manager.current = "dashboard"

        except Exception as exc:
            print("Dashboard back error:", exc)

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def open_menu(self, *args):
        """
        API عمومی برای باز کردن منو.
        """
        self._open_drawer()

    def close_menu(self, *args):
        """
        API عمومی برای بستن منو.
        """
        self._close_drawer()

    def toggle_menu(self, *args):
        """
        API عمومی برای تغییر وضعیت منو.
        """
        self._toggle_drawer()

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------

    def clear_content(self):
        """
        پاک کردن محتوای داخلی داشبورد.
        """
        try:
            if self.content_area:
                self.content_area.clear_widgets()
        except Exception as exc:
            print("Dashboard clear error:", exc)

    # ---------------------------------------------------------
    # Error protection
    # ---------------------------------------------------------

    def _safe_refresh(self, *args):
        """
        Refresh محافظت‌شده برای جلوگیری از کرش.
        """
        try:
            self.refresh()
        except Exception as exc:
            print("Safe dashboard refresh error:", exc)

    def __del__(self):
        """
        جلوگیری از خطا هنگام حذف آبجکت.
        """
        try:
            self.drawer_open = False
            self.drawer = None
            self.content_area = None
            self.welcome_label = None
            self.role_label = None
        except Exception:
            pass


