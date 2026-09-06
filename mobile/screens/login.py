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


        root.add_widget(
            self.identifier
        )

        root.add_widget(
            self.password
        )

        root.add_widget(
            self.status
        )

        root.add_widget(
            self.login_button
        )


        self.add_widget(
            root
        )


    # ==========================
    # STATUS
    # ==========================

    def _set_status(
        self,
        text,
        color=SECONDARY
    ):

        self.status.text = rtl_text(
            text
        )

        self.status.color = color



    # ==========================
    # LOGIN
    # ==========================

    def login(
        self,
        *_ 
    ):

        if self._busy:
            return


        identifier = (
            self.identifier.text.strip()
        )

        password = (
            self.password.text
        )


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


        self._busy = True


        self.login_button.disabled = True


        self._set_status(
            "در حال بررسی اطلاعات...",
            SECONDARY
        )


        Thread(
            target=self._authenticate,
            args=(
                identifier,
                password
            ),
            daemon=True
        ).start()



    # ==========================
    # AUTHENTICATION
    # ==========================

    def _authenticate(
        self,
        identifier,
        password
    ):

        try:

            # ======================
            # LOCAL TEST LOGIN
            # ======================

            if (
                identifier == "admin"
                and password == "1234"
            ):

                session = {

                    "user": {

                        "id": "local-admin",

                        "username": "admin",

                        "role": "manager",

                        "display_name":
                            "مدیر فراهوش"
                    },


                    "token":
                        "local-test-token"

                }


                if hasattr(
                    self.app_state,
                    "set_session"
                ):

                    self.app_state.set_session(
                        session
                    )

                else:

                    self.app_state.session = (
                        session
                    )



                Clock.schedule_once(
                    lambda dt:
                    self._login_success(),
                    0
                )


                return

            # ======================
            # SERVER LOGIN
            # ======================

            else:

                # فعلاً تا زمان اتصال API
                # ورود واقعی اینجا اضافه می‌شود

                Clock.schedule_once(
                    lambda dt:
                    self._login_failed(
                        "نام کاربری یا رمز عبور اشتباه است."
                    ),
                    0
                )


        except Exception as exc:

            print(
                "LOGIN ERROR:",
                repr(exc)
            )


            Clock.schedule_once(
                lambda dt:
                self._login_failed(
                    "خطا در ورود به سیستم"
                ),
                0
            )



    # ==========================
    # LOGIN SUCCESS
    # ==========================

    def _login_success(
        self
    ):

        self._busy = False

        self.login_button.disabled = False


        self._set_status(
            "ورود موفق",
            SUCCESS
        )


        try:

            self.manager.current = (
                "dashboard"
            )


        except Exception as exc:

            print(
                "DASHBOARD OPEN ERROR:",
                repr(exc)
            )


            self._set_status(
                "خطا در باز کردن صفحه اصلی",
                ERROR
            )



    # ==========================
    # LOGIN FAILED
    # ==========================

    def _login_failed(
        self,
        message
    ):

        self._busy = False

        self.login_button.disabled = False


        self._set_status(
            message,
            ERROR
        )
