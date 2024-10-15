車牌辨識系統

介紹

此專案是一個基於 Python 的車牌辨識系統，使用 Tkinter 創建 GUI 介面，並透過 Tesseract OCR 技術識別車牌號碼。系統會監控指定的資料夾，並自動辨識該資料夾中的圖片檔案（JPG, JPEG, PNG 格式）。辨識後，系統會顯示車牌號碼及相應的進出場時間，並顯示圖片。

功能

1. 車牌辨識：使用 Tesseract OCR 辨識車牌圖片中的文字。
2. 進出場記錄：當車輛進場時顯示入場時間，當車輛離場時顯示離場時間。
3. 圖片顯示：顯示進行辨識的車牌圖片。
4. 自動監控：系統會自動檢查資料夾內的圖片，每5秒鐘檢查一次，並進行車牌辨識。
5. 動態更新介面：透過 Tkinter 介面動態顯示最新的車牌號碼、進出場時間以及相關圖片。

安裝要求

- Python 3.x
- `pytesseract`：用於車牌辨識的 Tesseract OCR 庫
- `Pillow`：用於處理和顯示圖片的圖像處理庫
- `Tkinter`：用於創建 GUI 介面的庫

安裝依賴

你可以使用以下命令來安裝所需的庫：

bash
pip install pytesseract pillow


安裝 Tesseract

1. 下載並安裝 Tesseract OCR：[Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)
2. 安裝後，確認 Tesseract 安裝路徑並將其添加到系統環境變數中。
   - 例如，將以下路徑添加到環境變數 `TESSDATA_PREFIX`：
     ```
     C:\Program Files\Tesseract-OCR
     ```

使用方法

1. 修改資料夾路徑

在程式碼中找到 `myPath` 變數，將其設定為你要監控的圖片資料夾路徑：

```python
myPath = 'D:\\kevin data\\pythontest\\flask-chatbot\\pythonProject\\'
```

2. 啟動程式

運行程式後，將會顯示一個 Tkinter 視窗。你可以點擊「開始辨識」按鈕來啟動圖片處理過程。系統會自動監控指定的資料夾中的圖片檔案，並進行車牌識別，顯示車牌號碼和進出場時間。

3. 操作介面

- 車牌號碼顯示：顯示最新辨識出的車牌號碼。
- 入場/離場資訊：顯示車輛的進場或離場時間。
- 圖片顯示：顯示當前辨識的車牌圖片。

4. 停止系統

當不需要再進行車牌辨識時，直接關閉 Tkinter 視窗即可停止系統。

程式碼說明

- update_display(carPlate, actionTime, actionType, imagePath)：更新車牌號碼、進出場時間及顯示圖片。
- process_images()：檢查資料夾中的新圖片並使用 Tesseract 進行車牌識別。辨識結果將顯示在 Tkinter 視窗中，並且圖片處理後會被刪除以避免重複處理。
- startButton：觸發車牌辨識功能，開始監控資料夾。

注意事項

1. 圖片格式：系統目前僅支援 `.jpg`, `.jpeg`, 和 `.png` 格式的圖片。
2. 車牌識別精度：Tesseract 可能無法完美辨識所有車牌，對於特殊或不清晰的車牌可能識別效果不佳。
3. 資料夾清理：處理完的圖片會被自動刪除，請確保圖片資料夾中沒有重要的圖片檔案。
