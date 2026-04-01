# ai-email-responder

![Python](https://img.shields.io/badge/python-3.11+-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![Claude](https://img.shields.io/badge/AI-Claude%20%2F%20switchable-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

> AI-powered email reply generator with tone control, editable drafts, and optional SMTP sending. Supports Anthropic Claude, OpenAI, Groq, and Ollama — swap providers with one `.env` change.

## Features

- Paste any email → get an AI-drafted reply instantly
- 4 tone options: professional, friendly, concise, apologetic
- Fully editable draft before sending
- Optional SMTP email delivery
- Switchable AI provider — Claude, GPT, Groq, or Ollama
- Fully local mode via Ollama (no API key needed)

## Quick start

### 1. Clone and set up environment

```bash
git clone https://github.com/wahhabriaz/ai-email-responder
cd ai-email-responder
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

pip install -e .
```

### 2. Set up `.env`

```bash
cp .env.example .env
```

### 3. Run locally free with Ollama

Install Ollama from https://ollama.com/download then:

```bash
ollama pull llama3.2
```

Set your `.env`:

```env
ER_PROVIDER=ollama
ER_MODEL=llama3.2
ER_OLLAMA_BASE_URL=http://localhost:11434
ER_TONE=professional
```

### 4. Run the app

```bash
python app.py
```

Open http://localhost:7860 in your browser.

## How to use

1. Paste the email you received into the left box
2. Add any context (optional) — e.g. your refund policy
3. Choose a tone
4. Click **Generate draft**
5. Edit the draft on the right if needed
6. Fill in recipient email and subject
7. Click **Send email** (requires SMTP setup) or just copy the draft

## Tone options

| Tone         | Best for                              |
| ------------ | ------------------------------------- |
| Professional | Business emails, client communication |
| Friendly     | Casual replies, community messages    |
| Concise      | Quick confirmations, short answers    |
| Apologetic   | Complaints, delays, mistakes          |

## Switching AI providers

Change `ER_PROVIDER` in `.env`:

| Provider         | Value       | Model example             | API key needed  |
| ---------------- | ----------- | ------------------------- | --------------- |
| Ollama (local)   | `ollama`    | `llama3.2`                | No              |
| Anthropic Claude | `anthropic` | `claude-3-haiku-20240307` | Yes             |
| OpenAI           | `openai`    | `gpt-4o-mini`             | Yes             |
| Groq (free)      | `groq`      | `llama3-8b-8192`          | Yes (free tier) |

## Email sending setup (optional)

To enable actual email sending, set SMTP variables in `.env`:

```env
ER_SMTP_HOST=smtp.gmail.com
ER_SMTP_PORT=587
ER_SMTP_USER=you@gmail.com
ER_SMTP_PASS=your_16_char_app_password
```

For Gmail you need an **App Password** (not your login password):

1. Google Account → Security → Enable 2-Step Verification
2. Search "App Passwords" → Create one for Mail
3. Paste the 16-character code into `ER_SMTP_PASS`

Email sending is completely optional — you can use the tool just to generate drafts and copy them manually.

## Environment variables

| Variable               | Default                   | Description        |
| ---------------------- | ------------------------- | ------------------ |
| `ER_PROVIDER`          | `anthropic`               | AI provider        |
| `ER_MODEL`             | `claude-3-haiku-20240307` | Model name         |
| `ER_TONE`              | `professional`            | Default tone       |
| `ER_ANTHROPIC_API_KEY` | —                         | Anthropic API key  |
| `ER_OPENAI_API_KEY`    | —                         | OpenAI API key     |
| `ER_GROQ_API_KEY`      | —                         | Groq API key       |
| `ER_OLLAMA_BASE_URL`   | `http://localhost:11434`  | Ollama server URL  |
| `ER_SMTP_HOST`         | `smtp.gmail.com`          | SMTP server        |
| `ER_SMTP_PORT`         | `587`                     | SMTP port          |
| `ER_SMTP_USER`         | —                         | Your email address |
| `ER_SMTP_PASS`         | —                         | App password       |

## Project structure

```
ai-email-responder/
├── src/email_responder/
│   ├── __init__.py       # Settings
│   ├── providers.py      # Switchable AI clients
│   ├── drafter.py        # AI email drafter
│   ├── mailer.py         # SMTP sender
│   └── logger.py
├── app.py                # Gradio UI
└── .env.example
```

## Tech stack

Python 3.11 · Gradio · Anthropic · OpenAI · Groq · Ollama · SMTP
