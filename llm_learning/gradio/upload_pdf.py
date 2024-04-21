import gradio as gr
import os
import shutil


def process_file(filepath):
    path = "uploaded/" + os.path.basename(filepath)
    shutil.copyfile(src=filepath.name, dst=path)
    gr.Info("File uploaded!!")
    return path


callback = gr.CSVLogger()

with gr.Blocks() as demo:
    gr.Markdown('# Welcome to Upload Files!')
    with gr.Row():
        with gr.Column():
            file_output_pdf = gr.File(label='Upload pdf or word doc')
            upload_button_pdf = gr.UploadButton("Click to Upload a File", file_types=["file"], file_count="single")
            upload_button_pdf.upload(process_file, upload_button_pdf, file_output_pdf)
        with gr.Column():
            file_output_xml = gr.File(label='Upload xml file')
            upload_button_xml = gr.UploadButton("Click to Upload a File", file_types=["file"], file_count="single")
            upload_button_xml.upload(process_file, upload_button_xml, file_output_xml)
    with gr.Row():
        btn = gr.Button("Flag")

    # This needs to be called at some point prior to the first call to callback.flag()
    callback.setup(components=[file_output_pdf, file_output_xml], flagging_dir="flagged_demo")

    # We can choose which components to flag -- in this case, we'll flag all of them
    btn.click(fn=lambda *args: callback.flag(args), inputs=[file_output_pdf, file_output_xml],
              outputs=None, preprocess=False)
demo.launch()
