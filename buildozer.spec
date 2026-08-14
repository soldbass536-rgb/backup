[app]
title = My Backup
package.name = mybackup
package.domain = org.mybackup

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10, kivy, requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
