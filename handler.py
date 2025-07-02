import runpod
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import base64
import io

# 모델 로딩 (Serverless 컨테이너 시작 시 1회만 수행)
pipe = StableDiffusionPipeline.from_pretrained(
    "/mnt/vdb1/flux",  # 가중치 경로 (마운트된 경로에 맞게 수정)
    torch_dtype=torch.float16
).to("cuda")

def handler(job):
    try:
        input_data = job.get("input", {})
        prompt = input_data.get("prompt", "a cat in space")

        # 이미지 생성
        image: Image.Image = pipe(prompt).images[0]

        # base64 인코딩
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        encoded_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return {
            "output": {
                "output_base64": encoded_image
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
