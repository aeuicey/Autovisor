import os
import threading
import time


# 单例模式日志器
class Logger:
    _instance = None
    _lock = threading.Lock()  # 线程安全锁

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._init()
        return cls._instance

    def _init(self):
        os.makedirs("logs", exist_ok=True)  # 创建日志文件夹
        new_index = len(os.listdir("logs")) + 1
        self.filename = f"logs/Log{new_index}.txt"
        self.text = ""

    def write_log(self, msg):
        date = time.strftime("%H:%M:%S", time.localtime())
        self.text += f"[{date}] {msg}"

    def save(self, inform=True):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(self.text)
        if inform:
            print(f"日志文件已保存至: {self.filename}")

    def info(self, msg, shift=False):
        if shift:
            text = f"\r\n\033[32m[INFO]\033[0m {msg}"
        else:
            text = f"\r\033[32m[INFO]\033[0m {msg}"
        print(text.ljust(50))
        self.write_log(f"[INFO] {msg}\n")

    def warn(self, msg, shift=False):
        if shift:
            text = f"\r\n\033[33m[WARN]\033[0m {msg}"
        else:
            text = f"\r\033[33m[WARN]\033[0m {msg}"
        print(text.ljust(50))
        self.write_log(f"[WARN] {msg}\n")

    def error(self, msg, shift=False):
        if shift:
            text = f"\r\n\033[31m[ERROR]\033[0m {msg}"
        else:
            text = f"\r\033[31m[ERROR]\033[0m {msg}"
        print(text.ljust(50))
        self.write_log(f"[ERROR] {msg}\n")
