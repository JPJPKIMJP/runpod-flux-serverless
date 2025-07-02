import runpod

def handler(job):
    try:
        input_data = job.get("input", {})
        prompt = input_data.get("prompt", "test")
        
        return {
            "status": "success",
            "message": f"Handler working! Prompt: {prompt}",
            "input_received": input_data
        }
    except Exception as e:
        return {
            "status": "error", 
            "error": str(e)
        }

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
