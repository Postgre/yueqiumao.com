---
title: git中文显示问题解决
---
git中文不显示解决方法，设置这个后git就不会再对0x80以上的字符进行quote转换了

    git config --global core.quotepath false
