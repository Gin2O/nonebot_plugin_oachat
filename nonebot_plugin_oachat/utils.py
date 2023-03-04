import openai  # 导入 openai 库


class OpenApiChatbot:
    def __init__(self, api_key, model_id):
        # 初始化 OpenApiChatbot 类的实例
        # 参数 api_key 表示 OpenAI API 的凭据
        # 参数 model_id 表示要使用的模型 ID
        openai.api_key = api_key  # 设置 API 凭据
        self.model_id = model_id  # 设置模型 ID
        self.headers = {  # 构造请求头
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}"
        }

    def generate_response(self, prompt):
        # 根据输入的提示 prompt 生成 OpenApiChatbot 的回复文本
        data = {  # 构造请求数据
            "model": self.model_id,
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 1024
        }
        response = openai.Completion.create(  # 发送请求并获取响应
            model=data["model"],
            prompt=data["prompt"],
            temperature=data["temperature"],
            max_tokens=data["max_tokens"],
            top_p=1.0,
            n=1,
            stop=None,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        return response  # 返回响应中的完整文本

    # 定义一个函数，用于解析 ChatGPT API 的响应
    def analyze_chat_responses(self, prompt, response):

        chatResp = response.choices[0].text
        while (chatResp.startswith("\n") != chatResp.startswith("？") != chatResp.startswith(" ")):
            chatResp = chatResp[1:]

        # 补全问题
        completion_ques, chatResp = replace_completion_question(chatResp)

        while chatResp.startswith("\n"):
            chatResp = chatResp[1:]
        # 组合消息输出
        chatResp = prompt + completion_ques + "\n" + "oachat：" + "\n" + chatResp

        return chatResp

    # 定义一个函数，用于解析 ChatGPT API 的响应并获取所有输出结果
    def analyze_all_responses(self, resp):
        # 获取 def generate_response 响应的数据，并解析
        choices = resp['choices']
        # 创建一个列表，存储所有 ChatGPT 的输出结果
        allResp = []
        # 对响应中的 choices 列表进行迭代，获取所有结果的文本
        for choice in choices:
            allResp.append(choice['text'].strip())
        print(str(allResp))

        return allResp


# 未启用
def replace_first_short_string(text):

    import re

    target_str = ""
    # 定义匹配模式
    # 方法1 查找第一个符合条件的字符串

    # 方法2 使用正则表达式匹配第一个满足要求的字符串
    match = re.search(r'^[\u4e00-\u9fa5]{1,12}(?=\n)', text, flags=re.M)
    if match is not None:
        target_str = match.group()
        # 方法1：将找到的字符串替换为 "*"
        text = text.replace(target_str, "\n" + "*" * len(target_str), 1)
        # 方法2：将找到的字符串替换为 "*"
        # text = re.sub(target_str,  "\n" + "*" * len(target_str), text)

    # 返回替换后的字符串
    return text


def replace_completion_question(text):

    import re

    completion_ques = ""
    # 定义匹配模式
    # # 方法1 查找第一个符合条件的字符串 正则式有点问题

    # 方法2 使用正则表达式匹配第一个满足要求的字符串
    if is_chinese(text):
        # print('is_chinese')
        match = re.search(r'^[\u4e00-\u9fa5]{1,12}(?=\n)', text, flags=re.M)
        if match is not None:
            completion_ques = match.group()
            # 方法1：将找到的字符串替换为 "\n"
            text = text.replace(completion_ques, "", 1)

    elif is_english(text):
        # print('is_english')
        match = re.search(
            r"^(?:\s*[a-zA-Z]\w*(?:['’-]\w+)*\s){0,10}[a-zA-Z]\w*(?:['’-]\w+)*(?=\n)", text, flags=re.M)
        if match is not None:
            completion_ques = match.group()
            text = text.replace(completion_ques, "", 1)

            while completion_ques.startswith(" "):
                completion_ques = completion_ques[1:]
            completion_ques = " " + completion_ques

    # 返回替换后的字符串
    return completion_ques, text


def is_chinese(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False


def is_english(text):
    for char in text:
        if ('\u0041' <= char <= '\u005a') or ('\u0061' <= char <= '\u007a'):
            return True
    return False
