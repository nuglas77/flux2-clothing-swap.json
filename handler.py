import runpod
from comfyui_handler import ComfyUIHandler

# Initialize the ComfyUI handler with your full-graph workflow
comfy_handler = ComfyUIHandler(
    workflow_path="workflow.json",   # Must match the exact filename in the repo root
    input_mapping={
        "character_ref": "76.inputs.image",      # Character reference LoadImage
        "clothing_image": "81.inputs.image",     # Clothing LoadImage
        "prompt": "135.inputs.text",             # Prompt text
        "num_images": "129.inputs.batch_size"    # Batch size
    }
)

def handler(job):
    """Main handler for queue-based endpoint"""
    try:
        input_data = job["input"]
        
        # Run the workflow with injected inputs
        result = comfy_handler.run(input_data)
        
        return {
            "status": "success",
            "images": result.get("images", []),
            "message": f"Generated {len(result.get('images', []))} images"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Start the RunPod Serverless queue handler
runpod.serverless.start({"handler": handler})
