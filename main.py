from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from mobile.config import APP_NAME, BACKGROUND
from mobile.services.app_state import AppState
from mobile.ui import register_fonts

from mobile.screens.login import LoginScreen
from mobile.screens.dashboard import DashboardScreen
from mobile.screens.module import ModuleScreen
from mobile.screens.update import UpdateScreen


class FrahooshMobileApp(App):

    title = APP_NAME

    def build(self):

        Window.clearcolor = BACKGROUND

        try:
            register_fonts()
        except Exception as e:
            print("FONT ERROR:", e)

        try:
            self.state = None
            print("APP STATE DISABLED FOR TEST")

        manager = ScreenManager(
            transition=FadeTransition(duration=0.12)
        )

        screens = [
            ("login", LoginScreen),
            ("dashboard", DashboardScreen),
            ("module", ModuleScreen),
            ("update", UpdateScreen),
        ]

        for name, screen_class in screens:
            try:
                manager.add_widget(
                    screen_class(
                        self.state,
                        name=name
                    )
                )
                print("SCREEN OK:", name)

            except Exception as e:
                print("SCREEN ERROR:", name, e)

        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()           
