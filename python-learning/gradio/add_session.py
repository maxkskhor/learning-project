import gradio as gr
import pandas as pd


def collect(student, date, time, rate, comment):
    return pd.DataFrame({
        'student': [student],
        'date': [date],
        'time': [time],
        'rate': [rate],
        'comment': [comment]
    })


with gr.Blocks() as demo:
    gr.Markdown('# Add session: ')
    student = gr.Textbox(label='Student Name')
    with gr.Row():
        with gr.Column():
            date = gr.Textbox(label='Date')
        with gr.Column():
            time = gr.Textbox(label='Time')
        with gr.Column():
            rate = gr.Textbox(label='Rate')
    with gr.Row():
        with gr.Column(scale=4):
            comment = gr.Textbox(label='Comment')
        with gr.Column(scale=1):
            btn = gr.Button("Submit")
    btn.click(fn=collect, inputs=[student, date, time, rate, comment], outputs=[])

gr.close_all()
demo.launch(share=True)
