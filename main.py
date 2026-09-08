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

        # ثبت فونت
        try:
            register_fonts()

        except Exception as exc:
            print(
                "FONT ERROR:",
                repr(exc)
            )


        # وضعیت برنامه
        try:

            from mobile.services.app_state import AppState

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


        manager = ScreenManager(
            transition=FadeTransition(
                duration=0.15
            )
        )


        # -------------------------
        # LOGIN
        # -------------------------

        try:

            from mobile.screens.login import LoginScreen

            login = LoginScreen(
                app_state=self.state,
                name="login"
            )

            manager.add_widget(
                login
            )

            print(
                "LOGIN REGISTERED"
            )

        except Exception as exc:

            print(
                "LOGIN SCREEN ERROR:",
                type(exc).__name__,
                str(exc)
            )



        # -------------------------
        # DASHBOARD
        # -------------------------

        try:

            from mobile.screens.dashboard import DashboardScreen

            dashboard = DashboardScreen(
                app_state=self.state,
                name="dashboard"
            )


            manager.add_widget(
                dashboard
            )


            print(
                "DASHBOARD REGISTERED"
            )


        except Exception as exc:

            print(
                "DASHBOARD SCREEN ERROR:",
                type(exc).__name__,
                str(exc)
            )



        # -------------------------
        # MODULE
        # -------------------------

        try:

            from mobile.screens.module import ModuleScreen


            module = ModuleScreen(
                app_state=self.state,
                name="module"
            )


            manager.add_widget(
                module
            )


            print(
                "MODULE REGISTERED"
            )


        except Exception as exc:

            print(
                "MODULE SCREEN ERROR:",
                type(exc).__name__,
                str(exc)
            )



        # -------------------------
        # UPDATE
        # -------------------------

        try:

            from mobile.screens.update import UpdateScreen


            update = UpdateScreen(
                app_state=self.state,
                name="update"
            )


            manager.add_widget(
                update
            )


            print(
                "UPDATE REGISTERED"
            )


        except Exception as exc:

            print(
                "UPDATE SCREEN ERROR:",
                type(exc).__name__,
                str(exc)
            )



        # شروع برنامه

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
