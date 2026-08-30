import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from mobile.config import SUPABASE_URL, SUPABASE_ANON_KEY, API_TIMEOUT


class ApiError(RuntimeError):
    pass


class _Response:
    def __init__(self, status, body):
        self.status_code = status
        self._body = body or b""

    @property
    def ok(self):
        return 200 <= self.status_code < 300

    def json(self):
        if not self._body:
            return {}
        return json.loads(self._body.decode("utf-8"))

    def text(self):
        return self._body.decode("utf-8", errors="replace")


def _request(method, url, headers=None, payload=None, params=None, timeout=15):
    if params:
        url += ("&" if "?" in url else "?") + urlencode(params)
    data = None
    req_headers = dict(headers or {})
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req_headers["Content-Type"] = "application/json"
    request = Request(url, data=data, headers=req_headers, method=method)
    try:
        with urlopen(request, timeout=timeout) as response:
            return _Response(response.status, response.read())
    except HTTPError as exc:
        return _Response(exc.code, exc.read())
    except URLError as exc:
        raise ApiError(f"خطای اتصال به سرور: {exc.reason}") from exc
    except TimeoutError as exc:
        raise ApiError("زمان اتصال به سرور به پایان رسید.") from exc


class SupabaseClient:
    def __init__(self):
        self.url = SUPABASE_URL
        self.key = SUPABASE_ANON_KEY
        self.access_token = ""
        self.refresh_token = ""

    @property
    def configured(self):
        return bool(self.url and self.key)

    def _headers(self, authenticated=False):
        headers = {"apikey": self.key, "Content-Type": "application/json"}
        if authenticated and self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def sign_in(self, identifier, password):
        if not self.configured:
            raise ApiError("اتصال سرور در تنظیمات این نسخه فعال نشده است.")
        response = _request("POST", f"{self.url}/auth/v1/token?grant_type=password",
                            headers=self._headers(),
                            payload={"email": identifier, "password": password},
                            timeout=API_TIMEOUT)
        if not response.ok:
            raise ApiError(self._error(response, "ایمیل یا رمز عبور صحیح نیست."))
        data = response.json() or {}
        self.access_token = data.get("access_token", "")
        self.refresh_token = data.get("refresh_token", "")
        user = data.get("user") or {}
        return {"user": user, "profile": self._profile(user),
                "access_token": self.access_token, "refresh_token": self.refresh_token}

    def _profile(self, user):
        metadata = user.get("user_metadata") or {}
        profile = {k: metadata[k] for k in ("role", "display_name", "full_name", "username") if k in metadata}
        email = user.get("email", "")
        if not self.configured or not email:
            profile.setdefault("email", email)
            return profile
        try:
            response = _request("GET", f"{self.url}/rest/v1/account_settings",
                                headers=self._headers(True),
                                params={"email": f"eq.{email}", "limit": "1"},
                                timeout=API_TIMEOUT)
            if response.ok:
                rows = response.json() or []
                if rows and isinstance(rows[0], dict):
                    merged = dict(profile)
                    merged.update(rows[0])
                    return merged
        except Exception:
            pass
        profile.setdefault("email", email)
        profile.setdefault("username", email)
        profile.setdefault("display_name", email)
        return profile

    def table_select(self, table, params=None):
        if not self.configured or not self.access_token:
            raise ApiError("نشست معتبر نیست.")
        response = _request("GET", f"{self.url}/rest/v1/{table}",
                            headers=self._headers(True),
                            params=params or {"select": "*", "limit": "50"},
                            timeout=API_TIMEOUT)
        if not response.ok:
            raise ApiError(self._error(response))
        return response.json()

    def _error(self, response, default="خطای سرور"):
        try:
            payload = response.json() or {}
            return payload.get("message") or payload.get("error_description") or payload.get("msg") or payload.get("hint") or payload.get("details") or default
        except Exception:
            return f"{default} ({response.status_code})"

    def sign_out(self):
        if self.configured and self.access_token:
            try:
                _request("POST", f"{self.url}/auth/v1/logout", headers=self._headers(True), timeout=API_TIMEOUT)
            except Exception:
                pass
        self.access_token = ""
        self.refresh_token = ""
