from dotenv import load_dotenv
import os

# 加载.env配置
load_dotenv()
api_key = os.getenv("API_KEY")

def chat_agent():
    print("===== 三创Agent 对话程序 =====")
    print("输入exit退出\n")
    while True:
        user_input = input("你：")
        if user_input.strip().lower() == "exit":
            print("Agent：再见！")
            break
        # 这里后续对接大模型接口，现在先回显
        print(f"Agent：收到你的消息：{user_input}")

if __name__ == "__main__":
    chat_agent()