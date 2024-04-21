import numpy as np
import gradio as gr


def sepia(input_img, _strength):
    sepia_filter = _strength * np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    ) + (1 - _strength) * np.identity(3)
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


callback = gr.CSVLogger()

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            img_input = gr.Image()
            strength = gr.Slider(0, 1, 0.5)
        img_output = gr.Image()
    with gr.Row():
        btn = gr.Button("Flag")

    # This needs to be called at some point prior to the first call to callback.flag()
    callback.setup(components=[img_input, strength, img_output], flagging_dir="flagged_data_points")

    img_input.change(fn=sepia, inputs=[img_input, strength], outputs=img_output)
    strength.change(fn=sepia, inputs=[img_input, strength], outputs=img_output)

    # We can choose which components to flag -- in this case, we'll flag all of them
    btn.click(fn=lambda *args: callback.flag(args),
              inputs=[img_input, strength, img_output], outputs=None, preprocess=False)

demo.launch()
