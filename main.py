from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mobile.ui import register_fonts


class FrahooshMobileApp(App):

    title = "فراهوش"

    def build(self):
        Window.clearcolor = (0.965, 0.975, 0.985, 1)

        try:
            register_fonts()
        except Exception as exc:
            print("FONT ERROR:", repr(exc))

        try:
            from mobile.services.app_state import AppState
            self.state = AppState()
        except Exception as exc:
            print("APP STATE ERROR:", repr(exc))
            self.state = None

        manager = ScreenManager()

        from mobile.screens.login import LoginScreen
        from mobile.screens.dashboard import DashboardScreen
        from mobile.screens.module import ModuleScreen

        manager.add_widget(
            LoginScreen(self.state, name="login")
        )

        manager.add_widget(
            DashboardScreen(self.state, name="dashboard")
        )

        manager.add_widget(
            ModuleScreen(self.state, name="module")
        )

        try:
            from mobile.screens.update import UpdateScreen
            manager.add_widget(
                UpdateScreen(self.state, name="update")
            )
        except Exception as exc:
            print("UPDATE SCREEN ERROR:", repr(exc))

        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
