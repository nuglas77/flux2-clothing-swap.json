from runpod.serverless import start
from comfyui_handler import ComfyUIHandler

handler = ComfyUIHandler(
    workflow_path="workflow.json",   # or the exact name of your full-graph JSON in the repo
    input_mapping={
        "character_ref": "76.inputs.image",      # node 76 LoadImage
        "clothing_image": "81.inputs.image",     # node 81 LoadImage
        "prompt": "135.inputs.text",             # node 135 CLIPTextEncode
        "num_images": "129.inputs.batch_size"    # node 129 EmptyFlux2LatentImage
    }
)

start(handler)
