from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    print("三创Agent启动成功！")

if __name__ == "__main__":
    main()