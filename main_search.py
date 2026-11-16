from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")

URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

def chat_with_search():
    print("===== 三创Agent｜联网搜索对话版 =====")
    print("输入 exit 退出\n")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    msg_history = [
        {"role": "system", "content": "你是三创Agent，回答简洁准确，需要时调用联网搜索获取实时资料。"}
    ]

    while True:
        user_text = input("你：")
        if user_text.strip().lower() == "exit":
            print("Agent：再见！")
            break
        msg_history.append({"role": "user", "content": user_text})
        payload = {
            "model": ENDPOINT_ID,
            "messages": msg_history,
            "tools": [
                {
                    "type": "builtin_function",
                    "function": {"name": "search"}
                }
            ]
        }
        resp = requests.post(URL, headers=headers, json=payload, timeout=60)
        data = resp.json()
        answer = data["choices"][0]["message"]["content"]
        print(f"Agent：{answer}\n")
        msg_history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    chat_with_search()