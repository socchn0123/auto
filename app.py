import pyautogui
import keyboard
import tkinter as tk
from tkinter import ttk
import time
import threading

class AutoClicker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto Clicker")
        
        # キーとボタンの設定
        tk.Label(self, text="Key/Button:").grid(row=0, column=0, padx=10, pady=10)
        self.key_entry = tk.Entry(self)
        self.key_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # 押下間隔の設定 (ms)
        tk.Label(self, text="Press Interval (ms):").grid(row=1, column=0, padx=10, pady=10)
        self.press_interval = tk.IntVar(value=150)
        self.interval_entry = tk.Entry(self, textvariable=self.press_interval)
        self.interval_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # 開始ボタン
        start_button = tk.Button(self, text="Start", command=self.start_clicking)
        start_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        # 停止ボタン
        self.stop_event = threading.Event()
        stop_button = tk.Button(self, text="Stop", command=self.stop_clicking)
        stop_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # ホットキー（Ctrl + Shift + S）設定
        self.bind_all('<Control-Shift-Key-S>', self.stop_clicking)
        
        # 常に前面に表示
        self.attributes('-topmost', 1)

    def start_clicking(self):
        self.stop_event.clear()
        key = self.key_entry.get()
        interval = self.press_interval.get()
        
        # テキストボックスを無効化
        self.key_entry.config(state='disabled')
        self.interval_entry.config(state='disabled')
        
        # 自動クリックを別スレッドで実行
        thread = threading.Thread(target=self.click_loop, args=(key, interval, self.stop_event))
        thread.start()
    
    def click_loop(self, key, interval, stop_event):
        while not stop_event.is_set():
            self.click(key, interval)
    
    def click(self, key, interval):
        keyboard.press(key)
        self.precise_sleep(interval)
        keyboard.release(key)
    
    def precise_sleep(self, duration_ms):
        start = time.perf_counter()
        end = start + duration_ms / 1000.0
        while time.perf_counter() < end:
            pass
    
    def stop_clicking(self, event=None):
        self.stop_event.set()
        # スレッドが終了するまで待機
        time.sleep(self.press_interval.get() / 1000.0)
        # テキストボックスを再度有効化
        self.key_entry.config(state='normal')
        self.interval_entry.config(state='normal')

if __name__ == "__main__":
    app = AutoClicker()
    app.mainloop()
