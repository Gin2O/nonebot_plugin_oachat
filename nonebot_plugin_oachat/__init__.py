import aiohttp
import openai
import asyncio
import nonebot
from .utils import *


from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import (Message, MessageSegment)

# 读取配置
model_id = nonebot.get_driver().config.openai_api_modelid
try:
    api_key = nonebot.get_driver().config.openai_api_key
except:
    api_key = "没有api"
try:
    max_tokens = nonebot.get_driver().config.openai_max_tokens
except:
    max_tokens = 2000


oachat_on_command = nonebot.get_driver().config.oachat_on_command

__plugin_meta__ = PluginMetadata(
    name="OpenAI chatbot",
    description="没有上下文关联的OpenAI对话机器人",
    usage=(
        f"OpenAI chatbot： \n"
        f"    没有上下文关联的OpenAI对话机器人 \n \n"
        f" 1. /oachat <对话内容>\n"
        f" 2. {oachat_on_command} <对话内容> \n"
        f"        \n"
        f"model_id： {model_id}  \n"
    ),
)


# 实例化
oaBot = OpenApiChatbot(api_key, model_id)

# 定义命令
oachat = on_command(rf"{oachat_on_command}", aliases={
                    "/oachat"}, block=True, priority=5)


oachat_help = on_command(
    "/oachat_help", aliases={"/对话帮助"}, block=True, priority=5)


@oachat_help.handle()
async def _(msg: Message = CommandArg()):
    await oachat_help.finish(__plugin_meta__.usage)


@oachat.handle()
async def _(msg: Message = CommandArg()):
    if api_key == "没有api":
        await oachat.finish("请先配置openai_api_key")
    prompt = msg.extract_plain_text()
    if prompt == "" or prompt == None or prompt.isspace():
        await oachat.finish("输入东西啊喂！")
    await oachat.send(MessageSegment.text("Duang ing..."))
    loop = asyncio.get_event_loop()
    # 不同转递方法
    # try:
    #     res = await loop.run_in_executor(None, oaBot.analyze_chat_responses, oaBot.generate_response(prompt))
    # except Exception as e:
    #     await oachat.finish(str(e))
    # await oachat.finish(MessageSegment.text(res))
    try:
        res = await loop.run_in_executor(None, oaBot.generate_response, prompt)
    except Exception as e:
        await oachat.finish(str(e))
    await oachat.finish(MessageSegment.text(oaBot.analyze_chat_responses(res)))
