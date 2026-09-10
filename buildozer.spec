[app]

title = Frahoosh
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,otf,svg

source.exclude_exts = spec
source.exclude_dirs = bin,.buildozer,.git,__pycache__,tests


version = 1.1.0


requirements = python3,kivy==2.3.0,requests,urllib3,arabic-reshaper,python-bidi


orientation = portrait


android.permissions = INTERNET


android.api = 34
android.minapi = 23

android.ndk = 25c
android.ndk_api = 23

android.archs = arm64-v8a,armeabi-v7a


p4a.branch = master


fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1
