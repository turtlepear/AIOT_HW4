# AIOT_HW4 Chiikawa Generator (SD1.5 + LoRA)

這是一個基於 **Stable Diffusion 1.5** 與自訂 **LoRA 模型** 的 **Chiikawa 角色生成器**，使用 **Streamlit** 作為前端介面，方便互動式生成可愛的 Chiikawa 角色圖像。

由於模型等檔案容量太大，上傳不到github上，結果會以影片的方式呈現
---

## 功能特色

- 支援載入多個自訂(須自己訓練) LoRA 模型，控制角色風格  
- 調整生成步數（Steps）與 Guidance Scale  
- 支援批量生成多張圖片（Batch Size）  
- 調整 LoRA 權重，控制風格強弱  
- 生成圖像即時顯示於 Streamlit 網頁

---

## 系統需求

- Python 3.10+  
- GPU 建議 VRAM ≥ 8GB（RTX 3090 / A100 等）  
- CUDA 11+ 驅動  
- 建議在虛擬環境中安裝依賴

---


## 使用方式

啟動 Streamlit：

streamlit run app.py

操作步驟
選擇 LoRA 模型（可選）
輸入 Prompt，例如：
chiikawa\(a\),a cute bird chiikawa character, anime style

調整生成參數：
Steps（生成步數）：10~200
Guidance Scale（提示強度）：1~20
Batch Size（一次生成張數）：1~10

生成參數快速參考表
參數	範圍	推薦值	說明
Steps	10 ~ 200	30~50	推理步數，越高細節越好，但生成越慢
Guidance Scale	1.0 ~ 20.0	7.5	控制生成貼合 prompt 的程度
Batch Size	1 ~ 10	1~3	一次生成張數，受 GPU VRAM 限制

點擊 Generate，生成的圖片會即時顯示在網頁上
如果要存圖片檔，可在圖片上點擊右鍵


## 推薦 Prompt 範例

chiikawa\(a\), Chiikawa sitting with a dog, happy, chibi, cute
chiikawa\(a\), Chiikawa holding snack, cute pose, pastel colors
chiikawa\(a\), Chiikawa sleepy, hugging pillow, soft colors

## 注意事項

批量生成或高步數生成可能需要較多 GPU 記憶體
LoRA 權重過高可能導致風格過於固定，可依需求調整
建議使用 512x512 解析度生成圖片，較大解析度需更多 GPU VRAM
