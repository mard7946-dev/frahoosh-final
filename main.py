"""Android entrypoint for Frahoosh.

Buildozer packages the repository root so the existing ``mobile`` package
remains importable on Android exactly as it is during local development.
"""

from mobile.main import FrahooshMobileApp


if __name__ == "__main__":
    FrahooshMobileApp().run()
