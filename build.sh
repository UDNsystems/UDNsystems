#!/bin/bash
echo Compiling SCSS...
export PATH="./dart-sass:$PATH"
sass ./scss:./styling
echo Build complete.