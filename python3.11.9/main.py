"""入口文件 — Buildozer 要求 main.py"""
import sys, os, traceback

_CRASH_LOG = "/sdcard/jpstudy_crash.log"
try:
    from jp_study_kivy import JpApp
    JpApp().run()
except Exception:
    try:
        with open(_CRASH_LOG, "w") as f:
            traceback.print_exc(file=f)
    except:
        pass
    raise
