import os
from PIL import Image, ImageTk
import pytesseract
import time
import tkinter as tk
from tkinter import Label

carDict = {}
myPath = 'D:\\kevin data\\pythontest\\flask-chatbot\\pythonProject\\'

# 創建Tkinter視窗
root = tk.Tk()
root.title("車牌辨識系統")
root.geometry("600x600")

# 定義顯示車牌號碼與進出場資訊的Label
plateLabel = Label(root, text="車牌號碼:", font=("Arial", 16))
plateLabel.pack(pady=10)

entryLabel = Label(root, text="入場/離場資訊:", font=("Arial", 16))
entryLabel.pack(pady=10)

imageLabel = Label(root)
imageLabel.pack(pady=20)


# 更新顯示的車牌號碼與進出場時間
def update_display(carPlate, actionTime, actionType, imagePath):
    plateLabel.config(text=f"車牌號碼: {carPlate}")
    entryLabel.config(text=f"車輛{actionType}時間: {actionTime}")

    # 顯示圖片
    try:
        img = Image.open(imagePath)
        img = img.resize((300, 200))  # 調整圖片大小以適應視窗
        imgTk = ImageTk.PhotoImage(img)
        imageLabel.config(image=imgTk)
        imageLabel.image = imgTk  # 防止圖片被垃圾回收
    except Exception as e:
        print(f"無法顯示圖片 {imagePath}: {e}")


# 處理圖片與車牌辨識
def process_images():
    try:
        # 列出資料夾中的所有圖片檔案
        imageFiles = [f for f in os.listdir(myPath) if f.endswith(('.jpg', '.jpeg', '.png'))]

        if not imageFiles:
            print("沒有新圖片，等待中...")
            root.after(5000, process_images)  # 5秒後重新檢查
            return

        for imageFile in imageFiles:
            # 圖片完整路徑
            carPlatePath = os.path.join(myPath, imageFile)
            # 使用Tesseract進行車牌辨識
            try:
                keyText = pytesseract.image_to_string(Image.open(carPlatePath)).strip()
            except Exception as e:
                print(f"處理圖片 {imageFile} 時發生錯誤: {e}")
                continue

            if keyText in carDict:
                # 車輛已在場內，處理離場
                exitTime = time.asctime()
                print('車輛離場時間:', keyText, ':', exitTime)
                update_display(keyText, exitTime, "離場", carPlatePath)
                del carDict[keyText]
            else:
                # 車輛不在場內，處理入場
                entryTime = time.asctime()
                print('車輛入場時間:', keyText, ':', entryTime)
                update_display(keyText, entryTime, "入場", carPlatePath)
                carDict[keyText] = entryTime

            # 處理完該圖片後，將其刪除或移動到其他資料夾，避免重複處理
            os.remove(carPlatePath)

        # 繼續每5秒檢查一次資料夾
        root.after(5000, process_images)

    except Exception as e:
        print(f"處理圖片時發生錯誤: {e}")


# 啟動圖片處理的按鈕
startButton = tk.Button(root, text="開始辨識", command=lambda: root.after(100, process_images), font=("Arial", 14))
startButton.pack(pady=20)

# 啟動Tkinter主循環
root.mainloop()
