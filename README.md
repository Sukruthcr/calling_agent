#  AI-Powered Calling Agent

This project was built as part of the **AiKing Solutions Internship Pre-Qualification Task**.

## Features

- Outbound calling using **Twilio Voice API**
- Real-time **Text-to-Speech (TTS)** and **Speech-to-Text (STT)** via Whisper
- Automatic **call recording** and **local transcription**
- AI-generated **summary** using Hugging Face BART model
- 100% **local and free** (no paid API required for summarization)

---

##  Workflow

1. **Server Initialization**
   `node index.js` starts the Express server.

2. **Trigger Outbound Call**
   Run in another terminal:
   ```bash
   Invoke-WebRequest -Uri http://localhost:3000/make-call -Method POST

The AI bot makes a Twilio call to your verified number.

3. **Recording**
The call audio is automatically recorded and stored in your Twilio console.

4. **Transcription**
Once downloaded as recording.mp3, run:

python transcribe_whisper.py


Generates a text file: transcript_small.txt.

5. **AI Summarization**
Then run:

python ai_summary_local.py


Produces an AI-generated summary saved as summary_local.txt.

--> Tech Stack

Node.js – for backend & Twilio integration

Python – for AI processing

Twilio API – for outbound voice calls

Whisper (OpenAI) – for local speech-to-text

Hugging Face Transformers (BART) – for summarization

FFmpeg – for audio decoding

**.env var**
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
MY_PHONE_NUMBER=+91XXXXXXXXXX

**Example Workflow Diagram**

[User] → [Twilio Call (Voice)] → [Recording (MP3)]
           ↓
     [Whisper Transcription]
           ↓
     [Hugging Face Summarization]
           ↓
  [Transcript + Summary Saved Locally]