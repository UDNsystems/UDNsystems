#!/bin/bash
echo Compiling SCSS...
export PATH="./dart-sass:$PATH"
sass ./scss/style.scss:./styling/style.css
echo Compiling TypeScript...
cd ts
npm i --save-dev typescript
npx tsc
cd ..
echo Build complete.