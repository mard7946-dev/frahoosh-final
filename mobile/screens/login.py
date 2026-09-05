from threading import Thread

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp

from mobile.config import (
    APP_NAME,
    SYSTEM_TITLE,
    SCHOOL_NAME,
    PRIMARY,
    SECONDARY,
    SUCCESS,
    WHITE,
    ERROR,
)

from mobile.ui import (
    font_name,
    rtl_text,
    PersianTextInput,
)


class LoginScreen(Screen):

    def __init__(self, app_state, **kwargs):

        super().__init__(**kwargs)

        self.app_state = app_state
        self._busy = False

        self._build()


    def _build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=dp(24),
            spacing=dp(10),
        )


        root.add_widget(
            Label(
                text=rtl_text(APP_NAME),
                font_name=font_name(),
                font_size="34sp",
                bold=True,
                color=PRIMARY,
                size_hint_y=None,
                height=dp(52),
            )
        )


        root.add_widget(
            Label(
                text=rtl_text(SYSTEM_TITLE),
                font_name=font_name(),
                font_size="17sp",
                color=SECONDARY,
                size_hint_y=None,
                height=dp(40),
            )
        )


        root.add_widget(
            Label(
                text=rtl_text(SCHOOL_NAME),
                font_name=font_name(),
                font_size="13sp",
                color=PRIMARY,
                size_hint_y=None,
                height=dp(34),
            )
        )


        self.identifier = PersianTextInput(

            hint_text=rtl_text(
                "نام کاربری / ایمیل"
            ),

            multiline=False,

            size_hint_y=None,

            height=dp(52),

            halign="right",

            padding=[
                dp(12),
                dp(12)
            ],
        )


        self.password = PersianTextInput(

            hint_text=rtl_text(
                "رمز عبور"
            ),

            password=True,

            multiline=False,

            size_hint_y=None,

            height=dp(52),

            halign="right",

            padding=[
                dp(12),
                dp(12)
            ],
        )


        self.status = Label(

            text="",

            font_name=font_name(),

            font_size="12sp",

            color=SECONDARY,

            size_hint_y=None,

            height=dp(45),
        )


        self.login_button = Button(

            text=rtl_text(
                "ورود به فراهوش"
            ),

            font_name=font_name(),

            background_normal="",

            background_color=SUCCESS,

            color=WHITE,

            size_hint_y=None,

            height=dp(54),
        )


        self.login_button.bind(
            on_release=self.login
        )


        root.add_widget(self.identifier)

        root.add_widget(self.password)

        root.add_widget(self.status)

        root.add_widget(self.login_button)


        self.add_widget(root)

    # ==========================
    # LOGIN
    # ==========================

    def login(self, *_):

        if self._busy:
            return


        identifier = (
            self.identifier.text.strip()
        )

        password = self.password.text


        if not identifier or not password:

            self._set_status(
                "نام کاربری و رمز عبور را وارد کنید.",
                ERROR
            )

            return


        if self.app_state is None:

            self._set_status(
                "وضعیت برنامه آماده نیست.",
                ERROR
            )

            return


        # ==========================
        # LOCAL TEST LOGIN
        # ==========================

        if identifier == "admin" and password == "1234":

            self.app_state.role = "manager"

            self.app_state.display_name = (
                "مدیر فراهوش"
            )


            self._busy = False

            self.login_button.disabled = False


            self.login_button.text = rtl_text(
                "ورود به فراهوش"
            )


            self.manager.current = (
                "dashboard"
            )


            return



        # ==========================
        # SUPABASE LOGIN
        # ==========================


        if self.app_state.api is None:

            self._set_status(
                "سرویس اتصال به سرور ایجاد نشد.",
                ERROR
            )

            return



        if not self.app_state.api.configured:

            self._set_status(
                "تنظیمات اتصال به سرور فعال نیست.",
                ERROR
            )

            return



        self._busy = True


        self.login_button.disabled = True


        self.login_button.text = rtl_text(
            "در حال ورود..."
        )


        Thread(

            target=self._login_worker,

            args=(

                identifier,

                password,

            ),

            daemon=True,

        ).start()



    def _login_worker(
        self,
        identifier,
        password
    ):

        try:

            result = (
                self.app_state.api.sign_in(
                    identifier,
                    password
                )
            )


            Clock.schedule_once(

                lambda dt:
                self._login_success(result),

                0
            )


        except Exception as exc:


            Clock.schedule_once(

                lambda dt, msg=str(exc):
                self._login_failed(msg),

                0
            )



    def _login_success(self, payload):

        try:

            saved = (
                self.app_state.set_session(
                    payload
                )
            )


            if not saved:

                raise Exception(
                    "ذخیره نشست کاربر انجام نشد."
                )


            self.password.text = ""


            self._busy = False


            self.login_button.disabled = False


            self.login_button.text = rtl_text(
                "ورود به فراهوش"
            )



            if not self.manager.has_screen(
                "dashboard"
            ):


                from mobile.screens.dashboard import (
                    DashboardScreen
                )


                self.manager.add_widget(

                    DashboardScreen(

                        self.app_state,

                        name="dashboard"

                    )

                )



            dashboard = (
                self.manager.get_screen(
                    "dashboard"
                )
            )


            try:

                 dashboard.refresh()

            except Exception as exc:

                 print(
                      ‌ "DASHBOARD REFRESH ERROR:",
                         repr(exc)
                )


self.manager.current = "dashboard"



        except Exception as exc:

            self._login_failed(
                str(exc)
            )



    def _login_failed(self, message):

        self._busy = False


        self.login_button.disabled = False


        self.login_button.text = rtl_text(
            "ورود به فراهوش"
        )


        self._set_status(
            message or "ورود انجام نشد.",
            ERROR
        )



    def _set_status(
        self,
        message,
        color
    ):

        self.status.color = color


        self.status.text = rtl_text(
            message
            )
