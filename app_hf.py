import gradio as gr
from rembg import remove
from PIL import Image
import io

def remove_background(image):
    if image is None:
        return None
    
    # Convert to PIL Image if needed
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    
    # Remove background
    output = remove(image)
    
    return output

# Create Gradio interface
interface = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Image(type="pil", label="Background Removed"),
    title="Free Background Remover",
    description="Remove backgrounds from photos instantly using AI",
    examples=[]
)

if __name__ == "__main__":
    interface.launch()
