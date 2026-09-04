from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mobile.ui import register_fonts


class FrahooshMobileApp(App):

    title = "Frahoosh"

    def build(self):

        Window.clearcolor = (0.965, 0.975, 0.985, 1)

        # ثبت فونت قبل از ساخت Login
        try:
            register_fonts()
            print("FRAHOOSH: FONT OK")
        except Exception as e:
            print("FRAHOOSH: FONT ERROR:", repr(e))

        manager = ScreenManager()

        # فقط Login
        from mobile.screens.login import LoginScreen

        try:
            login = LoginScreen(None, name="login")
            manager.add_widget(login)
            manager.current = "login"

            print("FRAHOOSH: LOGIN OK")

        except Exception as e:
            print("FRAHOOSH: LOGIN ERROR:", repr(e))

            # صفحه اضطراری برای جلوگیری از خروج بی‌صدا
            from kivy.uix.label import Label

            manager.add_widget(
                Label(
                    text="Frahoosh\nLogin startup error",
                    font_size="22sp"
                )
            )

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
