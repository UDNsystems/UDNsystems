#!/bin/bash
echo Compiling SCSS...
export PATH="./dart-sass:$PATH"
sass ./scss/style.scss:./styling/style.css
echo Build complete.