import runpod
from comfyui_handler import ComfyUIHandler

# Initialize the handler with your workflow
handler = ComfyUIHandler(
    workflow_path="workflow.json",   # Make sure this matches the exact filename in your repo
    input_mapping={
        "character_ref": "76.inputs.image",      # Node 76 - Character reference
        "clothing_image": "81.inputs.image",     # Node 81 - Clothing image
        "prompt": "135.inputs.text",             # Node 135 - Prompt
        "num_images": "129.inputs.batch_size"    # Node 129 - Batch size
    }
)

# Start the RunPod Serverless handler
runpod.serverless.start(handler)
