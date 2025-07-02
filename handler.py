import runpod
import torch
from PIL import Image
import base64
import io

def handler(job):
    try:
        print("🟢 Handler 시작됨")

        image = Image.new("RGB", (512, 512), (255, 255, 255))
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return {"output": {"output_base64": encoded}}

    except Exception as e:
        print("❌ 오류 발생:", str(e))
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
