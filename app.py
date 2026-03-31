import gradio as gr
from email_responder.drafter import draft_reply, TONES
from email_responder.mailer import send_email
from email_responder import settings


def generate(original, context, tone):
    if not original.strip():
        return "Please paste an email to reply to."
    return draft_reply(original, context, tone)


def send(to, subject, body):
    if not to or not subject or not body:
        return "Please fill in all fields before sending."
    ok = send_email(to, subject, body)
    return "Email sent successfully!" if ok else "Failed to send — check SMTP settings."


with gr.Blocks(title="AI Email Responder", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# AI Email Responder")
    gr.Markdown(f"Provider: `{settings.provider}` · Model: `{settings.model}`")

    with gr.Row():
        with gr.Column():
            original = gr.Textbox(label="Original email", lines=8,
                                  placeholder="Paste the email you received...")
            context = gr.Textbox(label="Additional context (optional)", lines=2,
                                 placeholder="e.g. We offer a 30-day refund policy")
            tone = gr.Dropdown(list(TONES.keys()), value="professional", label="Tone")
            draft_btn = gr.Button("Generate draft", variant="primary")

        with gr.Column():
            draft = gr.Textbox(label="AI draft (editable)", lines=8)
            to = gr.Textbox(label="Send to (email address)")
            subject = gr.Textbox(label="Subject")
            send_btn = gr.Button("Send email", variant="secondary")
            status = gr.Textbox(label="Status", interactive=False)

    draft_btn.click(generate, [original, context, tone], draft)
    send_btn.click(send, [to, subject, draft], status)

if __name__ == "__main__":
    demo.launch()