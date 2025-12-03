# AIOT_HW4 Chiikawa Generator (SD1.5 + LoRA)

本專案開發一個基於 Stable Diffusion 1.5 與自訂 LoRA 模型 的 Chiikawa 角色生成器，並透Streamlit提供互動式操作介面。使用者可透過簡單的輸入框設定生成的 prompt、調整生成步數（Steps）、提示強度（Guidance Scale）、LoRA 權重與批量生成張數（Batch Size），快速產生符合期望風格的 Chiikawa 角色圖像。為了方便風格控制，本專案採用 LoRA 技術對 Stable Diffusion 模型進行微調，使生成結果保留原模型的穩定性，同時呈現訓練資料的特色風格。透過 WebUI 介面，使用者不需安裝複雜程式或指令操作，即可直接在網頁端輸入 prompt 並即時觀察生成結果，並可選擇下載圖片。專案同時提供推薦 prompt 範例與參數設定建議，以降低使用者上手難度。整體而言，本系統整合了 LoRA 模型微調與 WebUI 互動功能，提供一個簡單直覺、可生成高品質 Chiikawa 角色圖像的環境，適合個人創作或教育實驗使用。

Agent 對話過程
[Chiikawa LoRA 訓練指南.pdf](https://github.com/user-attachments/files/23901442/Chiikawa.LoRA.pdf)
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
```bash
streamlit run app.py
```

## 操作步驟
選擇 LoRA 模型（可選）
輸入 Prompt，例如：
```chiikawa\(a\),a cute bird chiikawa character, anime style```

調整生成參數
- **Steps（生成步數）**：10 ~ 200  
  > 控制推理步數，步數越高細節越好，但生成速度會變慢  
- **Guidance Scale（提示強度）**：1 ~ 20  
  > 控制生成結果貼合 Prompt 的程度，數值越高越符合輸入描述  
- **Batch Size（一次生成張數）**：1 ~ 10  
  > 一次生成的圖片張數，受 GPU VRAM 限制，建議 1~3 張為佳

生成參數快速參考表
| 參數           | 範圍         | 推薦值   | 說明                                  |
|----------------|------------|---------|-------------------------------------|
| Steps          | 10 ~ 200    | 30~50   | 推理步數，越高細節越好，但生成越慢       |
| Guidance Scale | 1.0 ~ 20.0 | 7.5     | 控制生成貼合 prompt 的程度              |
| Batch Size     | 1 ~ 10      | 1~3     | 一次生成張數，受 GPU VRAM 限制          |


點擊 Generate，生成的圖片會即時顯示在網頁上
如果要存圖片檔，可在圖片上點擊右鍵


## 推薦 Prompt 範例

- `chiikawa(a), Chiikawa sitting with a dog, happy, chibi, cute`
- `chiikawa(a), Chiikawa holding snack, cute pose, pastel colors`
- `chiikawa(a), Chiikawa sleepy, hugging pillow, soft colors`

## 結果(圖片 and 影片)

-  prompt : `chiikawa\(a\),a cute koala chiikawa character, real style`
<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/d2d14d40-031f-4a0c-a2c8-9b21eb40ff73" />

-  prompt : `chiikawa\(a\),a cute cat chiikawa character, real style`
<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/89d8d82a-a4a3-479b-a879-8f9083251d41" />

-  prompt : `chiikawa\(a\),a cute rabbit chiikawa character, real style`
<img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/c0863929-d7a9-45be-9a9b-96da94cf4e7b" />

-  網站demo影片
  
https://github.com/user-attachments/assets/5a7f5923-dfa2-43e1-b31c-5b7e143c90ee



## 注意事項

- 批量生成或高步數生成可能需要較多 GPU 記憶體
- LoRA 權重過高可能導致風格過於固定，可依需求調整
- 建議使用 512x512 解析度生成圖片，較大解析度需更多 GPU VRAM
