import gradio as gr
import os
import shutil


def process_file(filepath):
    path = "python_learning/gradio/uploaded/" + os.path.basename(filepath)
    shutil.copyfile(filepath.name, path)
    gr.Info("File uploaded!!")
    return path


# def upload_file(files):
#     file_paths = [file.name for file in files]
#     return file_paths

with gr.Blocks() as demo:
    gr.Markdown('# Welcome to Upload Files!')
    with gr.Row():
        with gr.Column():
            file_output = gr.File(label='Upload pdf or word doc')
            upload_button = gr.UploadButton("Click to Upload a File", file_types=["file"], file_count="single")
            upload_button.upload(process_file, upload_button, file_output)
        with gr.Column():
            file_output = gr.File(label='Upload xml file')
            upload_button = gr.UploadButton("Click to Upload a File", file_types=["file"], file_count="single")
            upload_button.upload(process_file, upload_button, file_output)
demo.launch()


# demo = gr.Interface(
#     fn=process_file,
#     inputs=[
#         "file",
#     ],
#     outputs="text"
# )
# demo.launch()
