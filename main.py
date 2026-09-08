from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import (
    ScreenManager,
    FadeTransition,
)

from mobile.ui import register_fonts


class FrahooshMobileApp(App):

    title = "فراهوش"

    def build(self):

        Window.clearcolor = (
            0.965,
            0.975,
            0.985,
            1
        )

        # -------------------------
        # Fonts
        # -------------------------

        try:

            register_fonts()

        except Exception as exc:

            print(
                "FONT REGISTER ERROR:",
                repr(exc)
            )


        # -------------------------
        # App State
        # -------------------------

        try:

            from mobile.services.app_state import (
                AppState
            )

            self.state = AppState()

            print(
                "APP STATE READY"
            )

        except Exception as exc:

            print(
                "APP STATE ERROR:",
                repr(exc)
            )

            self.state = None


        # -------------------------
        # Screen Manager
        # -------------------------

        manager = ScreenManager(
            transition=FadeTransition(
                duration=0.15
            )
        )


        # -------------------------
        # Login
        # -------------------------

        try:

            from mobile.screens.login import (
                LoginScreen
            )

            login = LoginScreen(
                self.state,
                name="login"
            )

            manager.add_widget(
                login
            )

            print(
                "LOGIN SCREEN READY"
            )


        except Exception as exc:

            print(
                "LOGIN LOAD ERROR:",
                repr(exc)
            )



        # -------------------------
        # Dashboard
        # -------------------------

        try:

            from mobile.screens.dashboard import (
                DashboardScreen
            )

            dashboard = DashboardScreen(
                self.state,
                name="dashboard"
            )

            manager.add_widget(
                dashboard
            )

            print(
                "DASHBOARD SCREEN READY"
            )


        except Exception as exc:

            print(
                "DASHBOARD LOAD ERROR:",
                repr(exc)
            )



        # -------------------------
        # Module
        # -------------------------

        try:

            from mobile.screens.module import (
                ModuleScreen
            )

            module = ModuleScreen(
                self.state,
                name="module"
            )

            manager.add_widget(
                module
            )

            print(
                "MODULE SCREEN READY"
            )


        except Exception as exc:

            print(
                "MODULE LOAD ERROR:",
                repr(exc)
            )



        # -------------------------
        # Update
        # -------------------------

        try:

            from mobile.screens.update import (
                UpdateScreen
            )

            update = UpdateScreen(
                self.state,
                name="update"
            )

            manager.add_widget(
                update
            )

            print(
                "UPDATE SCREEN READY"
            )


        except Exception as exc:

            print(
                "UPDATE LOAD ERROR:",
                repr(exc)
            )



        # -------------------------
        # Initial Screen
        # -------------------------

        if manager.has_screen(
            "login"
        ):

            manager.current = "login"

        elif manager.screen_names:

            manager.current = (
                manager.screen_names[0]
            )


        print(
            "SCREENS:",
            manager.screen_names
        )


        return manager



if __name__ == "__main__":

    FrahooshMobileApp().run()
