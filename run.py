# -*- coding: utf-8 -*-
import json
import re

import botpy
import requests
from botpy import errors
from botpy.message import Message
from botpy.types.message import Ark, ArkKv

class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        if '点歌' in message.content:
            command_len = message.content.split()
            if len(command_len) < 3:
                return await message.reply(content="模糊点歌: @我 点歌 歌名\n精确点歌: @我 点歌 歌名 歌手")
            suo_url = "https://suo.emobook.cn/api/creat.php"
            base_url = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
            music_data = requests.get(url=base_url, params={"key": command_len[2].strip()})
            music_datas = music_data.json()["data"]["song"]["itemlist"]
            try:
                music_name = music_datas[0]["name"]
                music_singer = music_datas[0]["singer"]
                music_url = "https://y.qq.com/n/ryqq/songDetail/" + music_datas[0]["mid"]
                music_mid = music_datas[0]["mid"]
                if len(command_len) > 3:
                    for music_data in music_datas:
                        if command_len[3].strip() in music_data["singer"]:
                            music_name = music_data["name"]
                            music_singer = music_data["singer"]
                            music_url = "https://y.qq.com/n/ryqq/songDetail/" + music_data["mid"]
                            music_mid = music_data["mid"]
            except IndexError:
                return await message.reply(content="未找到该音乐")
            params = {
                "dwz_title": "t_" + music_name,
                "dwz_reditype": 1,
                "dwz_yxq": "ever",
                "dwz_type": 1,
                "dwz_keynum": 5,
                "api_key": "NQXu4cmboG",
                "dwz_url": music_url,
            }
            music_url = requests.get(url=suo_url, params=params).json().get("url")
            image_res = requests.get("https://y.qq.com/n/ryqq/songDetail/" + music_mid).text
            img_data = json.loads(re.findall(r'window.__INITIAL_DATA__ ={"detail":(.*?),"songList"', image_res)[0])
            image_url = "https:" + img_data["picurl"].split('?')[0]
            params = {
                "dwz_title": "p_" + music_name,
                "dwz_reditype": 1,
                "dwz_yxq": "ever",
                "dwz_type": 1,
                "dwz_keynum": 5,
                "api_key": "NQXu4cmboG",
                "dwz_url": image_url,
            }
            image_url = requests.get(url=suo_url, params=params).json().get("url")
            payload: Ark = Ark(
                template_id=24,
                kv=[
                    ArkKv(key="#DESC#", value=music_singer),
                    ArkKv(key="#PROMPT#", value=f"点歌台 - {music_name}"),
                    ArkKv(key="#TITLE#", value=music_name),
                    ArkKv(key="#METADESC#", value="演唱: " + music_singer),
                    ArkKv(key="#IMG#", value=image_url),
                    ArkKv(key="#LINK#", value=music_url),
                ],
            )
            return await self.api.post_message(channel_id=message.channel_id, ark=payload, msg_id=message.id)
        elif '随机萌图' in message.content:
            try:
                image_url = requests.get("https://acg.toubiec.cn/random.php?ret=json").json()[0].get("imgurl")
                return await self.api.post_message(
                    channel_id=message.channel_id,
                    content="为你找到如下二次元图片",
                    image=image_url,
                    msg_id=message.id
                )
            except errors.ServerError:
                image_url = requests.get("https://acg.toubiec.cn/random.php?ret=json").json()[0].get("imgurl")
                return await self.api.post_message(
                    channel_id=message.channel_id,
                    content="为你找到如下二次元图片",
                    image=image_url,
                    msg_id=message.id
                )
        else:
            return await message.reply(content="我还没学会这个指令哦")

if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    intents = botpy.Intents.none()
    intents.public_guild_messages = True

    client = MyClient(intents=intents)
    client.run(appid="appid", token="token")