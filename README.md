<div align="center">

![botpy](https://socialify.git.ci/ReadSmall/music-bot/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=https%3A%2F%2Fgithub.com%2Ftencent-connect%2Fbot-docs%2Fblob%2Fmain%2Fdocs%2F.vuepress%2Fpublic%2Ffavicon-64px.png%3Fraw%3Dtrue&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)

[![Language](https://img.shields.io/badge/language-python-green.svg?style=plastic)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg?style=plastic)](https://github.com/tencent-connect/botpy/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![PyPI](https://img.shields.io/pypi/v/qq-botpy)
[![BK Pipelines Status](https://api.bkdevops.qq.com/process/api/external/pipelines/projects/qq-guild-open/p-713959939bdc4adca0eea2d4420eef4b/badge?X-DEVOPS-PROJECT-ID=qq-guild-open)](https://devops.woa.com/process/api-html/user/builds/projects/qq-guild-open/pipelines/p-713959939bdc4adca0eea2d4420eef4b/latestFinished?X-DEVOPS-PROJECT-ID=qq-guild-open)

_✨ 基于 [机器人开放平台API](https://bot.q.qq.com/wiki/develop/api/) 实现的机器人 ✨_

_✨ 为开发者提供一个简单的Demo,点歌机器人 ✨_

[爱发电](https://afdian.net/@nian-bot)
·
[开发者频道](https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=1MVLD4&appChannel=share&businessType=9&from=246610&biz=ka)

</div>

## 机器人指令

    /点歌 歌名
        模糊点歌
        示例：/点歌 李白
    /点歌 歌名 歌手
        精确点歌
        示例：/点歌 李白 李荣浩
    /随机萌图
        随机获取一张二次元图片
        示例：/随机萌图

## 使用方法

使用代码库前需要配置好相关的信息，可以跟随下面的步骤进行

### 环境安装

py包的依赖配置，通过`pip install -r requirements.txt` 可以安装所有的依赖包

### 运行机器人

在代码库根目录执行下面命令

```shell
python3 run.py
```

## 代码说明

    .
    ├── LICENSE
    ├── README.md
    ├── .gitignore 
    ├── requirements.txt    # py包的依赖配置，通过`pip install -r requirements.txt` 可以安装所有的依赖包
    ├── run.py              # 程序运行入口

## 特别感谢

-   [Python SDK](https://github.com/tencent-connect/botpy) 提供SDK

## 免责声明

数据来源：  

-   [QQ音乐](https://y.qq.com/)  提供点歌API
-   [苏晓晴](https://www.toubiec.cn/)  提供随机萌图API服务
