from kivy.animation import Animation
from kivy.graphics import Color, RoundedRectangle, Rectangle, Line
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screen import Screen
from kivy.uix.widget import Widget

from mobile.config import APP_NAME, SCHOOL_NAME


# ---------------------------------------------------------
# نقش‌ها
# ---------------------------------------------------------

ROLE_ALIASES = {
    "admin": "manager",
    "manager": "manager",
    "مدیر": "manager",
    "مدیریت": "manager",

    "executive": "executive",
    "معاون اجرایی": "executive",

    "educational": "educational",
    "training": "educational",
    "معاون آموزشی": "educational",

    "cultural": "cultural",
    "پرورشی": "cultural",
    "معاون پرورشی": "cultural",

    "advisor": "advisor",
    "counselor": "advisor",
    "مشاور": "advisor",

    "teacher": "teacher",
    "teacher_staff": "teacher",
    "دبیر": "teacher",

    "student": "student",
    "دانش‌آموز": "student",

    "parent": "parent",
    "parent_guardian": "parent",
    "guardian": "parent",
    "ولی": "parent",
}


ROLE_TITLES = {
    "manager": "مدیریت",
    "executive": "معاون اجرایی",
    "educational": "معاون آموزشی",
    "cultural": "معاون پرورشی",
    "advisor": "مشاوره",
    "teacher": "دبیر",
    "student": "دانش‌آموز",
    "parent": "ولی",
}


# ---------------------------------------------------------
# منوی مدیر
# ---------------------------------------------------------

MANAGER_MENU = [
    ("مدیریت", "management"),
    ("معاون آموزشی", "educational"),
    ("معاون اجرایی", "executive"),
    ("معاون پرورشی", "cultural"),
    ("مشاوره", "advisor"),
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


ROLE_MENU = {
    "executive": [
        ("معاون اجرایی", "executive"),
        ("دانش‌آموزان", "students"),
        ("اولیا", "parents"),
        ("صندوق پیام‌ها", "messages"),
        ("تنظیمات", "settings"),
        ("درباره برنامه", "about"),
    ],

    "educational": [
        ("معاون آموزشی", "educational"),
        ("دانش‌آموزان", "students"),
        ("دبیران", "teachers"),
        ("کلاس‌های آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("گزارش‌ها", "reports"),
        ("صندوق پیام‌ها", "messages"),
        ("درباره برنامه", "about"),
    ],

    "cultural": [
        ("معاون پرورشی", "cultural"),
        ("دانش‌آموزان", "students"),
        ("تابلو هوشمند", "smart_board"),
        ("صندوق پیام‌ها", "messages"),
        ("درباره برنامه", "about"),
    ],

    "advisor": [
        ("مشاوره", "advisor"),
        ("دانش‌آموزان", "students"),
        ("اولیا", "parents"),
        ("صندوق پیام‌ها", "messages"),
        ("درباره برنامه", "about"),
    ],

    "teacher": [
        ("پنل دبیر", "teacher"),
        ("دانش‌آموزان", "students"),
        ("کلاس‌های آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("صندوق پیام‌ها", "messages"),
        ("درباره برنامه", "about"),
    ],

    "student": [
        ("پنل دانش‌آموز", "student"),
        ("برنامه هفتگی", "schedule"),
        ("کلاس‌های آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("صندوق پیام‌ها", "messages"),
        ("درباره برنامه", "about"),
    ],

    "parent": [
        ("پنل اولیا", "parent"),
        ("برنامه و وضعیت تحصیلی", "student_info"),
        ("کلاس‌های آنلاین", "online"),
        ("تابلو هوشمند", "smart_board"),
        ("پرداخت کمک‌های داوطلبانه", "finance"),
        ("صندوق پیام‌ها", "messages"),
        ("درباره برنامه", "about"),
    ],
}


# ---------------------------------------------------------
# دکمه سه‌خطی واقعی
# ---------------------------------------------------------

class HamburgerButton(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            self._color = Color(
                1,
                1,
                1,
                1,
            )

            self._line1 = Line(
                width=2.2,
            )

            self._line2 = Line(
                width=2.2,
            )

            self._line3 = Line(
                width=2.2,
            )

        self.bind(
            pos=self._update_lines,
            size=self._update_lines,
        )

    def _update_lines(self, *_):

        x = self.x
        y = self.y

        w = self.width
        h = self.height

        left = x + w * 0.18
        right = x + w * 0.82

        y1 = y + h * 0.70
        y2 = y + h * 0.50
        y3 = y + h * 0.30

        self._line1.points = [
            left,
            y1,
            right,
            y1,
        ]

        self._line2.points = [
            left,
            y2,
            right,
            y2,
        ]

        self._line3.points = [
            left,
            y3,
            right,
            y3,
        ]


# ---------------------------------------------------------
# داشبورد
# ---------------------------------------------------------

class DashboardScreen(Screen):

    drawer_width = NumericProperty(0)

    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)

        self.app_state = app_state
        self.drawer_open = False

        self._build_ui()

    # -----------------------------------------------------
    # ساخت UI
    # -----------------------------------------------------

    def _build_ui(self):

        self.clear_widgets()

        self.root_layout = FloatLayout()

        # -------------------------------------------------
        # پس‌زمینه
        # -------------------------------------------------

        self.background = Image(
            source="assets/frahoosh_dashboard_background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={
                "x": 0,
                "y": 0,
            },
        )

        self.root_layout.add_widget(
            self.background
        )

        # -------------------------------------------------
        # لایه تیره خیلی ملایم برای خوانایی
        # -------------------------------------------------

        self.overlay_background = Widget()

        with self.overlay_background.canvas:
            self.overlay_color = Color(
                0.02,
                0.08,
                0.16,
                0.18,
            )

            self.overlay_rect = Rectangle(
                pos=self.overlay_background.pos,
                size=self.overlay_background.size,
            )

        self.overlay_background.bind(
            pos=self._update_overlay,
            size=self._update_overlay,
        )

        self.root_layout.add_widget(
            self.overlay_background
        )

        # -------------------------------------------------
        # هدر
        # -------------------------------------------------

        self.header = FloatLayout(
            size_hint=(1, None),
            height=dp(155),
            pos_hint={
                "top": 1,
            },
        )

        with self.header.canvas:
            self.header_color = Color(
                0.02,
                0.15,
                0.28,
                0.82,
            )

            self.header_rect = RoundedRectangle(
                pos=self.header.pos,
                size=self.header.size,
                radius=[
                    dp(0),
                ],
            )

        self.header.bind(
            pos=self._update_header,
            size=self._update_header,
        )

        self.root_layout.add_widget(
            self.header
        )

        # -------------------------------------------------
        # دکمه همبرگری
        # -------------------------------------------------

        self.menu_button = HamburgerButton(
            size_hint=(None, None),
            size=(
                dp(62),
                dp(62),
            ),
            pos_hint={
                "right": 0.98,
                "top": 0.94,
            },
        )

        self.menu_button.bind(
            on_touch_down=self._hamburger_touch
        )

        self.header.add_widget(
            self.menu_button
        )

        # -------------------------------------------------
        # عنوان
        # -------------------------------------------------

        self.title_label = Label(
            text="سامانه هوشمند مدیریت مدرسه",
            font_size="23sp",
            bold=True,
            color=(
                1,
                1,
                1,
                1,
            ),
            halign="right",
            valign="middle",
            size_hint=(0.78, None),
            height=dp(45),
            pos_hint={
                "right": 0.91,
                "top": 0.78,
            },
        )

        self.title_label.bind(
            size=self._sync_text_size
        )

        self.header.add_widget(
            self.title_label
        )

        # -------------------------------------------------
        # نام مدرسه
        # -------------------------------------------------

        self.school_label = Label(
            text=SCHOOL_NAME,
            font_size="15sp",
            color=(
                0.86,
                0.96,
                1,
                1,
            ),
            halign="right",
            valign="middle",
            size_hint=(0.78, None),
            height=dp(34),
            pos_hint={
                "right": 0.91,
                "top": 0.48,
            },
        )

        self.school_label.bind(
            size=self._sync_text_size
        )

        self.header.add_widget(
            self.school_label
        )

        # -------------------------------------------------
        # کارت خوش‌آمدگویی
        # -------------------------------------------------

        self.welcome_card = FloatLayout(
            size_hint=(0.90, None),
            height=dp(150),
            pos_hint={
                "center_x": 0.5,
                "top": 0.78,
            },
        )

        with self.welcome_card.canvas:
            self.welcome_color = Color(
                1,
                1,
                1,
                0.90,
            )

            self.welcome_rect = RoundedRectangle(
                pos=self.welcome_card.pos,
                size=self.welcome_card.size,
                radius=[
                    dp(22),
                ],
            )

        self.welcome_card.bind(
            pos=self._update_welcome,
            size=self._update_welcome,
        )

        self.root_layout.add_widget(
            self.welcome_card
        )

        self.welcome_title = Label(
            text="خوش آمدید 🌱",
            font_size="24sp",
            bold=True,
            color=(
                0.02,
                0.18,
                0.32,
                1,
            ),
            halign="right",
            valign="middle",
            size_hint=(0.88, None),
            height=dp(48),
            pos_hint={
                "right": 0.95,
                "top": 0.82,
            },
        )

        self.welcome_title.bind(
            size=self._sync_text_size
        )

        self.welcome_card.add_widget(
            self.welcome_title
        )

        self.role_label = Label(
            text="",
            font_size="16sp",
            color=(
                0.10,
                0.30,
                0.42,
                1,
            ),
            halign="right",
            valign="middle",
            size_hint=(0.88, None),
            height=dp(40),
            pos_hint={
                "right": 0.95,
                "top": 0.52,
            },
        )

        self.role_label.bind(
            size=self._sync_text_size
        )

        self.welcome_card.add_widget(
            self.role_label
        )

        # -------------------------------------------------
        # وضعیت
        # -------------------------------------------------

        self.status_label = Label(
            text="سامانه آماده استفاده است",
            font_size="14sp",
            color=(
                0.12,
                0.40,
                0.35,
                1,
            ),
            halign="right",
            valign="middle",
            size_hint=(0.88, None),
            height=dp(32),
            pos_hint={
                "right": 0.95,
                "top": 0.28,
            },
        )

        self.status_label.bind(
            size=self._sync_text_size
        )

        self.welcome_card.add_widget(
            self.status_label
        )

        # -------------------------------------------------
        # پنل راهنما
        # -------------------------------------------------

        self.hint_card = FloatLayout(
            size_hint=(0.90, None),
            height=dp(100),
            pos_hint={
                "center_x": 0.5,
                "y": 0.10,
            },
        )

        with self.hint_card.canvas:
            self.hint_color = Color(
                0.02,
                0.16,
                0.28,
                0.78,
            )

            self.hint_rect = RoundedRectangle(
                pos=self.hint_card.pos,
                size=self.hint_card.size,
                radius=[
                    dp(20),
                ],
            )

        self.hint_card.bind(
            pos=self._update_hint,
            size=self._update_hint,
        )

        self.root_layout.add_widget(
            self.hint_card
        )

        self.hint_label = Label(
            text="برای مشاهده امکانات سامانه، دکمه سه‌خطی بالای صفحه را لمس کنید.",
            font_size="14sp",
            color=(
                1,
                1,
                1,
                0.95,
            ),
            halign="center",
            valign="middle",
            size_hint=(0.90, 0.80),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5,
            },
        )

        self.hint_label.bind(
            size=self._sync_text_size
        )

        self.hint_card.add_widget(
            self.hint_label
        )

        # -------------------------------------------------
        # لایه منوی کناری
        # -------------------------------------------------

        self.drawer_overlay = Button(
            text="",
            background_normal="",
            background_color=(
                0,
                0,
                0,
                0.42,
            ),
            size_hint=(1, 1),
            pos_hint={
                "x": 0,
                "y": 0,
            },
            opacity=0,
            disabled=True,
        )

        self.drawer_overlay.bind(
            on_release=self.close_drawer
        )

        self.root_layout.add_widget(
            self.drawer_overlay
        )

        # -------------------------------------------------
        # منوی کشویی
        # -------------------------------------------------

        self.drawer = FloatLayout(
            size_hint=(None, 1),
            width=dp(315),
            x=-dp(315),
            pos_hint={
                "y": 0,
            },
        )

        with self.drawer.canvas:
            self.drawer_color = Color(
                0.025,
                0.10,
                0.18,
                0.98,
            )

            self.drawer_rect = RoundedRectangle(
                pos=self.drawer.pos,
                size=self.drawer.size,
                radius=[
                    dp(0),
                ],
            )

        self.drawer.bind(
            pos=self._update_drawer,
            size=self._update_drawer,
        )

        self.root_layout.add_widget(
            self.drawer
        )

        self._build_drawer()

        self.add_widget(
            self.root_layout
        )

    # -----------------------------------------------------
    # منوی کشویی
    # -----------------------------------------------------

    def _build_drawer(self):

        # عنوان منو
        menu_title = Label(
            text="فراهوش",
            font_size="25sp",
            bold=True,
            color=(
                1,
                1,
                1,
                1,
            ),
            size_hint=(1, None),
            height=dp(65),
            pos_hint={
                "top": 0.97,
            },
        )

        self.drawer.add_widget(
            menu_title
        )

        self.menu_role = Label(
            text="",
            font_size="14sp",
            color=(
                0.65,
                0.86,
                0.96,
                1,
            ),
            size_hint=(1, None),
            height=dp(34),
            pos_hint={
                "top": 0.91,
            },
        )

        self.drawer.add_widget(
            self.menu_role
        )

        # جداکننده
        separator = Widget(
            size_hint=(0.86, None),
            height=dp(1),
            pos_hint={
                "center_x": 0.5,
                "top": 0.86,
            },
        )

        with separator.canvas:
            Color(
                0.25,
                0.65,
                0.82,
                0.45,
            )

            self.separator_rect = Rectangle(
                pos=separator.pos,
                size=separator.size,
            )

        separator.bind(
            pos=lambda obj, value: setattr(
                self.separator_rect,
                "pos",
                value,
            ),
            size=lambda obj, value: setattr(
                self.separator_rect,
                "size",
                value,
            ),
        )

        self.drawer.add_widget(
            separator
        )

        self.menu_box = FloatLayout(
            size_hint=(1, None),
            height=dp(600),
            pos_hint={
                "x": 0,
                "top": 0.84,
            },
        )

        self.drawer.add_widget(
            self.menu_box
        )

        self.menu_buttons = []

    # -----------------------------------------------------
    # refresh
    # -----------------------------------------------------

    def refresh(self):

        role = self._get_role()

        display_name = self._get_display_name()

        role_title = ROLE_TITLES.get(
            role,
            "کاربر",
        )

        self.welcome_title.text = (
            f"خوش آمدید، {display_name}"
        )

        self.role_label.text = (
            f"نقش کاربری: {role_title}"
        )

        self.menu_role.text = (
            f"{display_name} | {role_title}"
        )

        self._populate_menu(role)

    # -----------------------------------------------------
    # ساخت منو بر اساس نقش
    # -----------------------------------------------------

    def _populate_menu(self, role):

        self.menu_box.clear_widgets()

        if role == "manager":
            items = MANAGER_MENU
        else:
            items = ROLE_MENU.get(
                role,
                [
                    ("درباره برنامه", "about"),
                ],
            )

        y = 1.0
        button_height = 0.085

        for title, route in items:

            button = Button(
                text=title,
                font_size="15sp",
                background_normal="",
                background_color=(
                    0.04,
                    0.22,
                    0.34,
                    1,
                ),
                color=(
                    1,
                    1,
                    1,
                    1,
                ),
                halign="right",
                valign="middle",
                size_hint=(0.88, None),
                height=dp(46),
                pos_hint={
                    "right": 0.94,
                    "top": y,
                },
            )

            button.bind(
                size=self._sync_text_size
            )

            button.bind(
                on_release=lambda btn, r=route:
                self._menu_selected(r)
            )

            self.menu_box.add_widget(
                button
            )

            self.menu_buttons.append(
                button
            )

            y -= button_height

        # خروج
        logout = Button(
            text="خروج از حساب",
            font_size="15sp",
            background_normal="",
            background_color=(
                0.55,
                0.12,
                0.14,
                1,
            ),
            color=(
                1,
                1,
                1,
                1,
            ),
            size_hint=(0.88, None),
            height=dp(48),
            pos_hint={
                "right": 0.94,
                "y": 0.025,
            },
        )

        logout.bind(
            on_release=self.logout
        )

        self.drawer.add_widget(
            logout
        )

        self.logout_button = logout

    # -----------------------------------------------------
    # کلیک همبرگر
    # -----------------------------------------------------

    def _hamburger_touch(self, widget, touch):

        if widget.collide_point(
            *touch.pos
        ):

            if touch.is_mouse_scrolling:
                return False

            self.toggle_drawer()

            return True

        return False

    # -----------------------------------------------------
    # باز / بسته شدن منو
    # -----------------------------------------------------

    def toggle_drawer(self):

        if self.drawer_open:
            self.close_drawer()
        else:
            self.open_drawer()

    def open_drawer(self, *_):

        self.drawer_open = True

        self.drawer_overlay.disabled = False
        self.drawer_overlay.opacity = 1

        Animation(
            x=0,
            duration=0.25,
            t="out_quad",
        ).start(
            self.drawer
        )

    def close_drawer(self, *_):

        self.drawer_open = False

        animation = Animation(
            x=-dp(315),
            duration=0.22,
            t="in_quad",
        )

        animation.bind(
            on_complete=self._drawer_closed
        )

        animation.start(
            self.drawer
        )

        self.drawer_overlay.disabled = True
        self.drawer_overlay.opacity = 0

    def _drawer_closed(self, *_):

        self.drawer.x = -dp(315)

    # -----------------------------------------------------
    # انتخاب منو
    # -----------------------------------------------------

    def _menu_selected(self, route):

        self.close_drawer()

        # -----------------------------
        # درباره برنامه
        # -----------------------------

        if route == "about":
            self._show_about()
            return

        # -----------------------------
        # صفحه مدیریت
        # -----------------------------

        if route == "management":

            self._go_to(
                "module",
                module="management",
            )

            return

        # -----------------------------
        # سایر پنل‌ها
        # -----------------------------

        route_map = {
            "educational": "educational",
            "executive": "executive",
            "cultural": "cultural",
            "advisor": "advisor",
            "parents": "parents",
            "parent": "parent",
            "students": "students",
            "student": "student",
            "teachers": "teachers",
            "teacher": "teacher",
            "finance": "finance",
            "online": "online",
            "smart_board": "smart_board",
            "ai": "ai",
            "messages": "messages",
            "settings": "settings",
            "reports": "reports",
            "schedule": "schedule",
            "student_info": "student_info",
        }

        module_name = route_map.get(
            route
        )

        if module_name:
            self._go_to(
                "module",
                module=module_name,
            )

    # -----------------------------------------------------
    # مسیریابی
    # -----------------------------------------------------

    def _go_to(self, screen_name, **kwargs):

        if not self.manager:
            return

        screen = self.manager.get_screen(
            screen_name
        )

        if hasattr(
            screen,
            "set_module",
        ):

            try:
                screen.set_module(
                    kwargs.get("module")
                )
            except Exception as exc:
                print(
                    "MODULE ROUTE ERROR:",
                    repr(exc),
                )

        elif hasattr(
            screen,
            "load_module",
        ):

            try:
                screen.load_module(
                    kwargs.get("module")
                )
            except Exception as exc:
                print(
                    "MODULE LOAD ERROR:",
                    repr(exc),
                )

        self.manager.current = screen_name

    # -----------------------------------------------------
    # درباره برنامه
    # -----------------------------------------------------

    def _show_about(self):

        self.close_drawer()

        self.status_label.text = (
            "فراهوش | سامانه مدیریت هوشمند مدارس"
        )

        self.hint_label.text = (
            "نام برنامه: فراهوش (سامانه مدیریت هوشمند مدارس)\n"
            "تولید کننده: حسن مردانه جهان تیغ\n"
            "سال تولید: ۱۴۰۵-۱۴۰۶"
        )

    # -----------------------------------------------------
    # خروج
    # -----------------------------------------------------

    def logout(self, *_):

        try:
            self.app_state.logout()
        except Exception as exc:
            print(
                "LOGOUT ERROR:",
                repr(exc),
            )

        self.close_drawer()

        if self.manager:
            self.manager.current = "login"

    # -----------------------------------------------------
    # نقش کاربر
    # -----------------------------------------------------

    def _get_role(self):

        role = None

        try:
            role = getattr(
                self.app_state,
                "role",
                None,
            )
        except Exception:
            role = None

        if not role:

            try:
                session = getattr(
                    self.app_state,
                    "session",
                    None,
                )

                if isinstance(
                    session,
                    dict,
                ):

                    user = session.get(
                        "user",
                        {},
                    )

                    if isinstance(
                        user,
                        dict,
                    ):

                        role = user.get(
                            "role"
                        )

            except Exception:
                role = None

        if not role:

            try:
                user = getattr(
                    self.app_state,
                    "user",
                    None,
                )

                if isinstance(
                    user,
                    dict,
                ):
                    role = user.get(
                        "role"
                    )

            except Exception:
                role = None

        role = (
            str(role).strip()
            if role
            else "student"
        )

        return ROLE_ALIASES.get(
            role,
            role,
        )

    # -----------------------------------------------------
    # نام کاربر
    # -----------------------------------------------------

    def _get_display_name(self):

        name = None

        try:
            name = getattr(
                self.app_state,
                "display_name",
                None,
            )
        except Exception:
            name = None

        if name:
            return str(name)

        try:

            session = getattr(
                self.app_state,
                "session",
                None,
            )

            if isinstance(
                session,
                dict,
            ):

                user = session.get(
                    "user",
                    {},
                )

                if isinstance(
                    user,
                    dict,
                ):

                    for key in (
                        "display_name",
                        "full_name",
                        "name",
                        "username",
                    ):

                        value = user.get(
                            key
                        )

                        if value:
                            return str(
                                value
                            )

        except Exception:
            pass

        return "کاربر فراهوش"

    # -----------------------------------------------------
    # آپدیت Canvas
    # -----------------------------------------------------

    def _update_overlay(self, instance, value):

        self.overlay_rect.pos = value
        self.overlay_rect.size = instance.size

    def _update_header(self, instance, value):

        self.header_rect.pos = value
        self.header_rect.size = instance.size

    def _update_welcome(self, instance, value):

        self.welcome_rect.pos = value
        self.welcome_rect.size = instance.size

    def _update_hint(self, instance, value):

        self.hint_rect.pos = value
        self.hint_rect.size = instance.size

    def _update_drawer(self, instance, value):

        self.drawer_rect.pos = value
        self.drawer_rect.size = instance.size

    def _sync_text_size(self, instance, value):

        instance.text_size = value

    # -----------------------------------------------------
    # ورود به صفحه
    # -----------------------------------------------------

    def on_pre_enter(self, *args):

        try:
            self.refresh()
        except Exception as exc:
            print(
                "DASHBOARD REFRESH ERROR:",
                repr(exc),
            )

        return super().on_pre_enter(
            *args
        )

    def on_leave(self, *args):

        if self.drawer_open:
            self.close_drawer()

        return super().on_leave(
            *args
        )     
                                                
