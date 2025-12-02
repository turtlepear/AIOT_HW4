import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from pathlib import Path
from PIL import Image

# -----------------------------
# 模型設定
# -----------------------------
MODEL_ID = "runwayml/stable-diffusion-v1-5"  # SD1.5 官方模型
LORA_DIR = "AIOT_HW/HW4/website/model"       # 放 LoRA 的資料夾

# -----------------------------
# 載入模型
# -----------------------------
@st.cache_resource
def load_pipe():
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        safety_checker=None
    )
    pipe = pipe.to("cuda")
    return pipe

pipe = load_pipe()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Chiikawa Generator (SD1.5)")

# 選擇 LoRA（可選）
lora_files = [f.name for f in Path(LORA_DIR).glob("*.safetensors")]
lora_choice = st.selectbox("Select LoRA", ["None"] + lora_files)

# Prompt
prompt = st.text_area("Prompt", "a cute chiikawa character, anime style")

# 步數與 guidance
num_inference_steps = st.slider("Steps", min_value=10, max_value=200, value=50)
guidance_scale = st.slider("Guidance Scale", min_value=1.0, max_value=20.0, value=7.5)

# 批量生成
batch_size = st.number_input("Batch Size", min_value=1, max_value=10, value=1)

# 生成按鈕
if st.button("Generate"):
    images = []

    for i in range(batch_size):
        # 載入 LoRA，如果選擇了
        if lora_choice != "None":
            lora_path = str(Path(LORA_DIR) / lora_choice)
            pipe.load_lora_weights(lora_path, weight=0.8)  # 權重可調整 0.8~1.0

        # 生成圖像
        result = pipe(prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale)
        image = result.images[0]
        images.append(image)

    # 顯示圖像
    for idx, img in enumerate(images):
        st.image(img, caption=f"Generated Image {idx+1}", use_container_width=True)

    st.success(f"Generated {batch_size} image(s)!")
