from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mobile.ui import register_fonts


class FrahooshMobileApp(App):

    title = "Frahoosh"

    def build(self):

        Window.clearcolor = (0.965, 0.975, 0.985, 1)

        # فونت
        try:
            register_fonts()
            print("FRAHOOSH: FONT OK")
        except Exception as e:
            print("FRAHOOSH: FONT ERROR:", repr(e))

        # ساخت وضعیت برنامه
        try:
            from mobile.services.app_state import AppState

            self.state = AppState()

            if self.state.api is None:
                print("FRAHOOSH: API NOT CREATED")
            else:
                print("FRAHOOSH: APP STATE OK")

        except Exception as e:
            print("FRAHOOSH: APP STATE ERROR:", repr(e))
            self.state = None

        manager = ScreenManager()

        # Login
        from mobile.screens.login import LoginScreen

        login = LoginScreen(
            self.state,
            name="login"
        )

        manager.add_widget(login)
        manager.current = "login"

        print("FRAHOOSH: LOGIN OK")

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
