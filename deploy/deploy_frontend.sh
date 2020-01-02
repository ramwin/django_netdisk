#!/bin/bash
# Xiang Wang @ 2019-10-15 22:23:49

mv music/dist ./
rm -rf yinyuebang/static/
mv dist/index.html  yinyuebang/account/templates/account/index.html
mv dist yinyuebang/static
sh yinyuebang/deploy/restart.sh
