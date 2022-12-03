import gradio as gr

from modules import script_callbacks
import modules.shared as shared

from PIL import Image


def on_ui_tabs():
    with gr.Blocks() as gti_interface:
        with gr.Row(equal_height=True):
            with gr.Column(variant='panel'):
                with gr.Column(variant='panel'):
                    output_dir = gr.Textbox(label="Output directory", placeholder="Output directory", value="")
                    number_of_generation = gr.Textbox(label="number_of_generation", placeholder="Number of generation", value="")
                    width = gr.Textbox(label="width", placeholder="width", value="512")
                    height = gr.Textbox(label="height", placeholder="height", value="512")
            with gr.Column(variant='panel'):
                status = gr.Textbox(label="", interactive=False, show_progress=True)
                
        
        dir_run = gr.Button(elem_id="dir_run", label="Generate", variant='primary')
        
        dir_run.click(
            fn=main,
            inputs=[output_dir, number_of_generation, width, height],
            outputs=[status]
        )

      
    return (gti_interface, "Genarate TransparentIMG", "gti_interface"),


script_callbacks.on_ui_tabs(on_ui_tabs)


def main(output_dir, number_of_generation, width, height):

    img = Image.new("RGBA", (int(width), int(height)), color=0)

    for num in range(int(number_of_generation)):
        img.save(output_dir + "/" + "transparent_" + str((num+1)) + ".png", quality=95)
    print("Genarated_tarnsparent_images")
    return "Genarated tarnsparent images"