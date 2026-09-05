import json
import os
from pathlib import Path


APP_NAME = "فراهوش"
SYSTEM_TITLE = "سامانه هوشمند آموزشی یکپارچه"

APP_VERSION = "1.1.1"

PACKAGE_NAME = "ir.frahoosh"
DEVELOPER_NAME = "تیم توسعه فراهوش"


BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"

RUNTIME_CONFIG_FILE = BASE_DIR / "runtime_config.json"


def _read_runtime_config():

    try:
        if RUNTIME_CONFIG_FILE.exists():

            data = json.loads(
                RUNTIME_CONFIG_FILE.read_text(
                    encoding="utf-8"
                )
            )

            if isinstance(data, dict):
                return data

    except Exception:
        pass

    return {}



_RUNTIME = _read_runtime_config()



def _setting(name, default=""):

    value = os.getenv(name)

    if value:
        return value.strip()


    value = _RUNTIME.get(
        name,
        default
    )


    if value is None:
        return default


    return str(value).strip()



# ============================
# Backend / Supabase
# ============================


SUPABASE_URL = _setting(
    "FRAHOOSH_SUPABASE_URL",
    ""
).rstrip("/")


SUPABASE_ANON_KEY = _setting(
    "FRAHOOSH_SUPABASE_ANON_KEY",
    ""
)

print("SUPABASE URL:", SUPABASE_URL)
print(
    "SUPABASE KEY:",
    "OK" if SUPABASE_ANON_KEY else "EMPTY"
)



SCHOOL_ID = _setting(
    "FRAHOOSH_SCHOOL_ID",
    "frahoosh-school"
)



SCHOOL_NAME = _setting(
    "FRAHOOSH_SCHOOL_NAME",
    "دبیرستان سردار شهید حاجی‌زاده ۲"
)



SCHOOL_YEAR = _setting(
    "FRAHOOSH_SCHOOL_YEAR",
    "۱۴۰۵ - ۱۴۰۶"
)



try:

    API_TIMEOUT = float(
        _setting(
            "FRAHOOSH_API_TIMEOUT",
            "15"
        )
    )

except Exception:

    API_TIMEOUT = 15



# ============================
# Assets
# ============================


FONT_REGULAR = str(
    ASSETS_DIR /
    "NotoSansArabic-Regular.ttf"
)


FONT_BOLD = str(
    ASSETS_DIR /
    "NotoSansArabic-Bold.ttf"
)


LOGO_PATH = str(
    ASSETS_DIR /
    "frahoosh_logo.png"
)



# ============================
# UI Colors
# ============================


PRIMARY = (
    0.059,
    0.09,
    0.165,
    1
)


SECONDARY = (
    0.118,
    0.227,
    0.545,
    1
)


SUCCESS = (
    0.086,
    0.639,
    0.325,
    1
)


BACKGROUND = (
    0.965,
    0.975,
    0.985,
    1
)


WHITE = (
    1,
    1,
    1,
    1
)


TEXT = (
    0.08,
    0.10,
    0.14,
    1
)


MUTED = (
    0.38,
    0.42,
    0.48,
    1
)


ERROR = (
    0.75,
    0.12,
    0.12,
    1
)


CARD = (
    1,
    1,
    1,
    1
)


BORDER = (
    0.86,
    0.89,
    0.93,
    1
)
