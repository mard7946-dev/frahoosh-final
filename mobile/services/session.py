import json
import os
from pathlib import Path


# ============================================================
# Frahoosh Mobile
# Android-safe Session Storage
# ============================================================

def _session_file():
    """
    محل امن ذخیره Session.

    روی Android نباید کنار سورس برنامه بنویسیم.
    Kivy App.user_data_dir محل مناسب و قابل نوشتن است.
    """

    try:
        from kivy.app import App

        app = App.get_running_app()

        if app is not None:
            base = Path(app.user_data_dir)
        else:
            base = Path.home() / ".frahoosh"

    except Exception:
        base = Path.home() / ".frahoosh"

    base.mkdir(
        parents=True,
        exist_ok=True
    )

    return base / "session.json"


def _atomic_write(path, content):
    """
    نوشتن امن Session.
    """

    temp = path.with_suffix(".tmp")

    try:
        temp.write_text(
            content,
            encoding="utf-8"
        )

        os.replace(
            str(temp),
            str(path)
        )

        return True

    except OSError:

        try:
            if temp.exists():
                temp.unlink()
        except OSError:
            pass

        return False


def save_session(data: dict):
    """
    ذخیره نشست کاربر.
    """

    if not isinstance(data, dict):
        return False

    try:

        session_file = _session_file()

        content = json.dumps(
            data,
            ensure_ascii=False,
            separators=(",", ":")
        )

        return _atomic_write(
            session_file,
            content
        )

    except (
        OSError,
        TypeError,
        ValueError
    ):
        return False


def load_session():
    """
    بازیابی نشست قبلی کاربر.

    Session خراب یا بدون Access Token
    معتبر محسوب نمی‌شود.
    """

    try:

        session_file = _session_file()

        if not session_file.exists():
            return None

        raw = session_file.read_text(
            encoding="utf-8"
        )

        data = json.loads(raw)

        if not isinstance(data, dict):
            return None

        access_token = data.get(
            "access_token"
        )

        if not access_token:
            return None

        return data

    except (
        FileNotFoundError,
        json.JSONDecodeError,
        UnicodeDecodeError,
        OSError,
        TypeError,
        ValueError
    ):
        return None


def update_session_tokens(
    access_token,
    refresh_token=None,
    expires_in=None,
    expires_at=None,
    token_type=None
):
    """
    به‌روزرسانی Tokenهای نشست.
    """

    session = load_session()

    if not isinstance(session, dict):
        session = {}

    if access_token:
        session["access_token"] = access_token

    if refresh_token:
        session["refresh_token"] = refresh_token

    if expires_in is not None:
        session["expires_in"] = expires_in

    if expires_at is not None:
        session["expires_at"] = expires_at

    if token_type:
        session["token_type"] = token_type

    return save_session(session)


def clear_session():
    """
    حذف کامل Session.
    """

    try:

        session_file = _session_file()

        if session_file.exists():
            session_file.unlink()

        return True

    except OSError:
        return False          
