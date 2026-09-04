from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from mobile.config import APP_NAME, BACKGROUND
from mobile.ui import register_fonts

from mobile.screens.login import LoginScreen
from mobile.screens.dashboard import DashboardScreen
from mobile.screens.module import ModuleScreen
from mobile.screens.update import UpdateScreen


class FrahooshMobileApp(App):

    title = APP_NAME

    def build(self):

        Window.clearcolor = BACKGROUND

        # -------------------------------------------------
        # فونت
        # -------------------------------------------------
        try:
            register_fonts()
            print("FRAHOOSH: FONT OK")
        except Exception as e:
            print("FRAHOOSH: FONT ERROR:", repr(e))

        # -------------------------------------------------
        # AppState
        # -------------------------------------------------
        try:
            from mobile.services.app_state import AppState

            self.state = AppState()

            print("FRAHOOSH: APP STATE OK")

        except Exception as e:

            print(
                "FRAHOOSH: APP STATE ERROR:",
                repr(e)
            )

            self.state = None

        # -------------------------------------------------
        # ScreenManager
        # -------------------------------------------------
        manager = ScreenManager(
            transition=FadeTransition(duration=0.12)
        )

        # -------------------------------------------------
        # LOGIN
        # Login باید همیشه ساخته شود
        # -------------------------------------------------
        try:

            login = LoginScreen(
                self.state,
                name="login"
            )

            manager.add_widget(login)

            print("FRAHOOSH: LOGIN OK")

        except Exception as e:

            print(
                "FRAHOOSH: LOGIN ERROR:",
                repr(e)
            )

        # -------------------------------------------------
        # Dashboard
        # فقط اگر AppState سالم باشد
        # -------------------------------------------------
        if self.state is not None:

            try:

                dashboard = DashboardScreen(
                    self.state,
                    name="dashboard"
                )

                manager.add_widget(dashboard)

                print("FRAHOOSH: DASHBOARD OK")

            except Exception as e:

                print(
                    "FRAHOOSH: DASHBOARD ERROR:",
                    repr(e)
                )

        # -------------------------------------------------
        # Module
        # -------------------------------------------------
        if self.state is not None:

            try:

                module = ModuleScreen(
                    self.state,
                    name="module"
                )

                manager.add_widget(module)

                print("FRAHOOSH: MODULE OK")

            except Exception as e:

                print(
                    "FRAHOOSH: MODULE ERROR:",
                    repr(e)
                )

        # -------------------------------------------------
        # Update
        # -------------------------------------------------
        if self.state is not None:

            try:

                update = UpdateScreen(
                    self.state,
                    name="update"
                )

                manager.add_widget(update)

                print("FRAHOOSH: UPDATE OK")

            except Exception as e:

                print(
                    "FRAHOOSH: UPDATE ERROR:",
                    repr(e)
                )

        # -------------------------------------------------
        # شروع مستقیم از Login
        # -------------------------------------------------
        if manager.has_screen("login"):

            manager.current = "login"

            print("FRAHOOSH: START LOGIN")

        return manager


if __name__ == "__main__":
    try:

        FrahooshMobileApp().run()

    except Exception as e:

        print(
            "FRAHOOSH: FATAL ERROR:",
            repr(e)
        )

        raise
                
