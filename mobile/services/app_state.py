from mobile.services.api import SupabaseClient
from mobile.services.session import load_session, save_session, clear_session


class AppState:
    def __init__(self):
        self.api = SupabaseClient()
        try:
            self.session = load_session() or {}
        except Exception:
            self.session = {}
        self._sync_tokens()

    def _sync_tokens(self):
        self.api.access_token = str(self.session.get("access_token", "") or "")
        self.api.refresh_token = str(self.session.get("refresh_token", "") or "")

    @property
    def logged_in(self):
        return bool(self.session and self.api.access_token)

    @property
    def user(self):
        value = self.session.get("user") if self.session else {}
        return value if isinstance(value, dict) else {}

    @property
    def profile(self):
        value = self.session.get("profile") if self.session else {}
        return value if isinstance(value, dict) else {}

    @property
    def role(self):
        metadata = self.user.get("user_metadata") or {}
        role = self.profile.get("role") or metadata.get("role") or self.user.get("role") or "student"
        return str(role).strip().lower()

    @property
    def display_name(self):
        metadata = self.user.get("user_metadata") or {}
        return (self.profile.get("display_name") or self.profile.get("full_name") or
                metadata.get("display_name") or metadata.get("full_name") or
                self.profile.get("username") or self.user.get("email") or "کاربر فراهوش")

    @property
    def email(self):
        return str(self.user.get("email") or self.profile.get("email") or "")

    def set_session(self, payload):
        self.session = payload if isinstance(payload, dict) else {}
        self._sync_tokens()
        save_session(self.session)

    def logout(self):
        try:
            self.api.sign_out()
        except Exception:
            pass
        clear_session()
        self.session = {}
        self._sync_tokens()
