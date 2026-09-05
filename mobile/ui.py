from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase

from mobile.config import (
    FONT_REGULAR,
    FONT_BOLD,
)


_FONT_READY = False


def register_fonts():

    global _FONT_READY

    if _FONT_READY:
        return FONT_REGULAR


    LabelBase.register(
        name="Frahoosh",
        fn_regular=FONT_REGULAR,
        fn_bold=FONT_BOLD,
    )

    _FONT_READY = True

    return "Frahoosh"



def font_name():

    return register_fonts()



class PersianTextInput(TextInput):

    def __init__(self, **kwargs):

        register_fonts()

        kwargs.setdefault(
            "font_name",
            "Frahoosh"
        )

        kwargs.setdefault(
            "halign",
            "right"
        )

        kwargs.setdefault(
            "cursor_width",
            2
        )

        super().__init__(**kwargs)



def rtl_text(text):

    return text[::-1]    
