from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager


class FrahooshMobileApp(App):

    title = "Frahoosh"

    def build(self):
        Window.clearcolor = (0.965, 0.975, 0.985, 1)
        manager = ScreenManager()

        # فقط Login در شروع برنامه ساخته می‌شود.
        # هیچ Dashboard / Module / Update / AppState در startup اجرا نمی‌شود.
        from mobile.screens.login import LoginScreen

        login = LoginScreen(None, name="login")
        manager.add_widget(login)
        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()           
                
