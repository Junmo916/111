[app]

title = jpstudy

package.name = jpstudy
package.domain = org.reasonix

version = 1.0.0

source.dir = python3.11.9
source.main = jp_study_kivy.py

requirements = python3,kivy

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
#android.gradle_dependencies =

orientation = portrait
fullscreen = 0
android.permissions =
android.allow_backup = True
android.wakelock = False
android.console = False
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
