from transformers import pipeline


print(" Loading local summarization model (BART)...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

with open("transcript_small.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

print("🎧 Summarizing the transcript...")


summary = summarizer(transcript, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]

print("\n AI Summary:\n")
print(summary)

with open("summary_local.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print("\n Summary saved as summary_local.txt")
