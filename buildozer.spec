[app]

# 应用名（手机桌面显示）
title = jpstudy

# 包名（唯一标识）
package.name = jpstudy
package.domain = org.reasonix

# 应用版本号
version = 1.0.0

# 源码目录（相对于 buildozer.spec）
source.dir = python3.11.9

# 启动脚本
source.main = jp_study_kivy.py

# Python 依赖（buildozer 会自动编译）
requirements = python3,kivy

# Android API 版本
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
# android.gradle_dependencies =
# android.gradle_options = --warning-mode all

# 屏幕方向
orientation = portrait

# 全屏（隐藏系统状态栏）
fullscreen = 0

# 权限（本应用不需要网络，只读写自己的数据目录）
android.permissions =

# 图标（留空则用默认图标）
# icon = icon.png

# CI 中自动接受 SDK 许可
android.accept_sdk_license = True



# 其他
android.allow_backup = True
android.wakelock = False
android.console = False

[buildozer]

# 日志级别
log_level = 2

# WSL / 交叉编译输出目录
warn_on_root = 1

# 每次构建前是否清理
# clean = 0


