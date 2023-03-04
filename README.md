<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot_plugin_oachat

_✨ NoneBot openai api ——简单的调用接口  ✨_

<a href="https://pypi.org/project/nonebot-plugin-oachat">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-note.svg" alt="pypi">
</a>

</div>


# 安装

* pip 
```
pip install nonebot-plugin-oachat
```

* nb_cli
```
nb plugin install nonebot-plugin-oachat
```

# 配置.env

```
# ====== WULUN_OACHATBOT ======   # 没有上下文的OPENAI
oachat_on_command = /chat

OPENAI_API_KEY = sk-************************************************
OPENAI_API_MODELID = "text-davinci-003"
OPENAI_MAX_TOKENS = 1000
```



# 使用
```
nonebot.load_plugin('nonebot_plugin_oachat')
```


# 命令
**注：使用命令时需要加命令前缀** 

* ```
  使用 /chat + 对话即可
  ```
  
  


# 其他

有bug有什么想法都可以告诉我，可先用e-mail联系：wulun0102@outlook.com

## 更新记录
- 2023.0303 更新OpenAI回复逻辑的补全问题，详情参照[issue-01](https://github.com/Gin2O/nonebot_plugin_oachat/issues/1) 


- 本项目只是为了一个简单可分离的接口，以便接入后续的新api



# 🐦 TODO list

- [ ] 加入上下文对话；
- [ ] 适配ChatGPT API；
- [ ] 搞到本地模型；
- [ ] 增解除文本输出限制；



## 特别鸣谢：

- None