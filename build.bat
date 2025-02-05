@echo off
IF NOT EXIST "build\NUL" mkdir "build"

blender --command extension build --source-dir ./source --output-dir ./build --verbose