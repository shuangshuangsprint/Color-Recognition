import pyautogui
import tkinter as tk
from threading import Thread
import time

# 获取鼠标位置的颜色
def get_pixel_color(x, y):
    screenshot = pyautogui.screenshot()
    r, g, b = screenshot.getpixel((x, y))
    return r, g, b

# 更新颜色显示的函数
def update_color_label(label):
    while True:
        x, y = pyautogui.position()
        color = get_pixel_color(x, y)
        color_text = f"位置: ({x}, {y})\n颜色: R={color[0]}, G={color[1]}, B={color[2]}"
        label.config(text=color_text, bg=f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')
        time.sleep(0.1)  # 每0.1秒更新一次

# 主函数
def main():
    root = tk.Tk()
    root.title("实时颜色显示")

    # 创建显示颜色的标签
    color_label = tk.Label(root, text="", font=("Helvetica", 12), width=30, height=5)
    color_label.pack(pady=20)

    # 创建一个线程实时更新颜色
    thread = Thread(target=update_color_label, args=(color_label,))
    thread.daemon = True
    thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
