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

    def analyze_chat_responses(self, resp):

        chatResp = resp.choices[0].text
        # 移除所有开头的\n
        while (chatResp.startswith("\n") != chatResp.startswith("？")):
            chatResp = chatResp[1:]
        print(str(chatResp))

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
