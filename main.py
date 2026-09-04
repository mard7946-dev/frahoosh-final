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

        # پس زمینه برنامه
        Window.clearcolor = BACKGROUND

        # ثبت فونت
        try:
            register_fonts()
        except Exception:
            pass


        # ساخت وضعیت برنامه
        try:
            self.state = AppState()

        except Exception:
            self.state = None


        # مدیریت صفحات
        manager = ScreenManager(
            transition=FadeTransition(
                duration=0.12
            )
        )


        # ورود
        manager.add_widget(
            LoginScreen(
                self.state,
                name="login"
            )
        )


        # داشبورد
        manager.add_widget(
            DashboardScreen(
                self.state,
                name="dashboard"
            )
        )


        # ماژول ها
        manager.add_widget(
            ModuleScreen(
                self.state,
                name="module"
            )
        )


        # بروزرسانی
        manager.add_widget(
            UpdateScreen(
                self.state,
                name="update"
            )
        )


        # شروع برنامه
        manager.current = "login"


        return manager



if __name__ == "__main__":
    FrahooshMobileApp().run()
