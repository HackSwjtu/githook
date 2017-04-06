# Hackswjtu - Githook

![](https://img.shields.io/badge/HackSwjtu-Githook-green.svg)
![](https://img.shields.io/badge/license-MIT-green.svg?style=flat)

```
     _/                            _/
    _/_/_/      _/_/_/    _/_/_/  _/  _/
   _/    _/  _/    _/  _/        _/_/
  _/    _/  _/    _/  _/        _/  _/
 _/    _/    _/_/_/    _/_/_/  _/    _/
```

## 描述

Hackswjtu 自用 Githook。在进行 `git commit` 操作时，向指定的成员发送邮件，描述本次修改时当前条记录的 `git log -p` 信息，便捷快速的进行 *Coding Review*。

## 配置方法

### macOS & Linux

在拥有 *git* 功能的项目目录中（即含有 `.git` 目录），执行安装命令：

```bash
$ curl -s hackswjtu.com/hook.sh | bash
```

按照提示输入 `sudo` 密码，看到以下图样完成 hook 配置。该脚本由于需要在 `.git/hooks/` 中增添文件，需要获取文件的读写权限，故需要 `sudo` 密码校验。

![](screenshot.png)

## MIT License

Copyright (c) 2017 Hack Swjtu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.






