[app]

title = Frahoosh
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = mobile

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,otf,ico,svg

source.exclude_exts = spec

source.exclude_dirs = bin,.buildozer,.git,__pycache__,tests

version = 1.0.0

requirements = python3==3.11.10,kivy==2.3.1,requests==2.32.3,arabic-reshaper==3.0.0,python-bidi==0.6.6

orientation = portrait

fullscreen = 0


# =========================================================
# ANDROID
# =========================================================

android.api = 35
android.minapi = 24

android.ndk = 28c
android.ndk_api = 24

android.archs = arm64-v8a

android.private_storage = True

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.enable_androidx = True

android.entrypoint = org.kivy.android.PythonActivity


# =========================================================
# PYTHON FOR ANDROID
# =========================================================

p4a.bootstrap = sdl2

p4a.fork = kivy

p4a.branch = develop

p4a.commit = 5865575


[buildozer]

log_level = 2
warn_on_root = 1
