# QQ频道机器人-点歌助手

该代码库是基于QQ机器人框架进行开发的机器人，用于服务点歌

赞助开发者：[爱发电](https://afdian.net/@nian-bot)

开发者频道：[点击加入开发者QQ频道](https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=1MVLD4&appChannel=share&businessType=9&from=246610&biz=ka)

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