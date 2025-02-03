#!/bin/bash
if [ ! -d "build" ]; then
    mkdir build
fi

blender --command extension build --source-dir ./source --output-dir ./build --verbose