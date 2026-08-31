import json
from pathlib import Path


def _session_file():
    try:
        from kivy.app import App
        app = App.get_running_app()
        if app is not None and app.user_data_dir:
            return Path(app.user_data_dir) / "session.json"
    except Exception:
        pass
    return Path(__file__).resolve().parent.parent / "storage" / "session.json"


def save_session(data: dict):
    if not isinstance(data, dict):
        data = {}
    try:
        path = _session_file()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    except (OSError, TypeError, ValueError):
        pass


def load_session():
    try:
        path = _session_file()
        if not path.exists():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else None
    except (FileNotFoundError, json.JSONDecodeError, OSError, UnicodeDecodeError, TypeError, ValueError):
        return None


def clear_session():
    try:
        path = _session_file()
        if path.exists():
            path.unlink()
    except OSError:
        pass
