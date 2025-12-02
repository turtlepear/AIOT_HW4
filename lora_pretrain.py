# from diffusers import StableDiffusionXLPipeline
# import torch

# pipe = StableDiffusionXLPipeline.from_pretrained(
#     "AIOT_HW/HW4/website/model/sdxl_base_1.0",
#     torch_dtype=torch.float16,
#     safety_checker=None
# )
# pipe.to("cuda")

# # 如果你有 SDXL LoRA
# pipe.load_lora_weights("AIOT_HW/HW4/website/model/tkw1.safetensors", weight=1.0)


# prompt = "tkw animal 2d illustration smile"
# image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
# image.show()  # 在本地打開生成的圖


from diffusers import StableDiffusionPipeline
import torch

MODEL_ID = "runwayml/stable-diffusion-v1-5"  # SD1.5 官方模型

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    safety_checker=None
)

pipe.to("cuda")
