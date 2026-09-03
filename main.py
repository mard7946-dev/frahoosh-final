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
    """
    نقطه ورود اصلی اپلیکیشن فراهوش.

    ترتیب اجرای برنامه:
        1. راه‌اندازی محیط Kivy
        2. ثبت فونت
        3. ایجاد وضعیت برنامه
        4. نمایش مستقیم صفحه ورود

    LoadingScreen عمداً از مسیر startup حذف شده است تا قبل از
    نمایش Login هیچ Thread یا عملیات شبکه‌ای اجرا نشود.
    """

    title = APP_NAME

    def build(self):
        # رنگ پس‌زمینه اصلی برنامه
        Window.clearcolor = BACKGROUND

        # ثبت فونت؛ در صورت بروز مشکل فونت، خود برنامه نباید Crash کند.
        try:
            register_fonts()
        except Exception:
            pass

        # ایجاد وضعیت برنامه
        #
        # AppState در حالت عادی باید بدون خطا ساخته شود.
        # اگر به هر دلیل مقداردهی اولیه آن با مشکل مواجه شد،
        # LoginScreen همچنان باید قابل نمایش باشد.
        try:
            self.state = AppState()
        except Exception:
            self.state = None

        # ایجاد ScreenManager
        manager = ScreenManager(
            transition=FadeTransition(duration=0.12)
        )

        # صفحه ورود، اولین صفحه واقعی برنامه است.
        manager.add_widget(
            LoginScreen(
                self.state,
                name="login"
            )
        )

        # داشبورد پس از ورود موفق
        manager.add_widget(
            DashboardScreen(
                self.state,
                name="dashboard"
            )
        )

        # صفحه ماژول‌ها
        manager.add_widget(
            ModuleScreen(
                self.state,
                name="module"
            )
        )

        # صفحه بروزرسانی
        manager.add_widget(
            UpdateScreen(
                self.state,
                name="update"
            )
        )

        # برنامه مستقیماً با Login شروع می‌شود.
        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
