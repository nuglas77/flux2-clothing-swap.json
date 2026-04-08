import runpod
import json
import base64
from comfyui_handler import ComfyUIHandler

def handler(job):
    try:
        input_data = job["input"]
        
        # Map inputs to your workflow nodes
        workflow = input_data.get("workflow", {})  # fallback if needed
        
        # Override the key nodes
        # Node 76 - Character reference (LoadImage)
        if "character_ref" in input_data:
            workflow["76"]["inputs"]["image"] = input_data["character_ref"]
        
        # Node 81 - Clothing image (LoadImage)
        if "clothing_image" in input_data:
            workflow["81"]["inputs"]["image"] = input_data["clothing_image"]
        
        # Node 135 - Prompt
        if "prompt" in input_data:
            workflow["135"]["inputs"]["text"] = input_data["prompt"]
        
        # Node 129 - Batch size
        if "num_images" in input_data:
            workflow["129"]["inputs"]["batch_size"] = input_data["num_images"]
        
        # Run the workflow
        result = ComfyUIHandler.run_workflow(workflow)
        
        return {
            "status": "success",
            "images": result.get("images", []),
            "message": "Generation completed"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Start the Serverless handler
runpod.serverless.start({"handler": handler})
