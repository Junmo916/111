"""入口文件 — Buildozer 要求 main.py"""
import sys, os, traceback

try:
    from jp_study_kivy import JpApp
    JpApp().run()
except Exception:
    with open(os.path.join(os.path.expanduser("~"), "jpstudy_crash.log"), "w") as f:
        traceback.print_exc(file=f)
    raise
