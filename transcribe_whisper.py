import whisper
import os
import sys
import time

def transcribe_with_model(model_size="small"):
    try:
        start_time = time.time()
        print(f" Loading {model_size} Whisper model...")

        os.environ["WHISPER_CACHE_DIR"] = os.path.join(os.path.expanduser("~"), ".cache", "whisper")
        os.makedirs(os.environ["WHISPER_CACHE_DIR"], exist_ok=True)
        

        model = whisper.load_model(model_size)
        model_load_time = time.time() - start_time

        
        audio_path = r"c:\Users\sukru\Downloads\record.mp3.wav"

        if not os.path.exists(audio_path):
            print(f" Error: Audio file not found at {audio_path}")
            return

        print("🎧 Transcribing, please wait...")
        transcribe_start = time.time()
        result = model.transcribe(audio_path)
        transcribe_time = time.time() - transcribe_start

        print("\n Transcription Result:")
        print(result["text"])

        
        output_file = f"transcript_{model_size}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        total_time = time.time() - start_time
        print(f"\n⚡ Performance Metrics:")
        print(f"Model Load Time: {model_load_time:.2f}s")
        print(f"Transcription Time: {transcribe_time:.2f}s")
        print(f"Total Time: {total_time:.2f}s")
        print(f"\n Transcript saved as {output_file}")

    except Exception as e:
        print(f" Error: {str(e)}")
        print("\nDebug information:")
        print(f"Python version: {sys.version}")
        print(f"Whisper cache directory: {os.environ.get('WHISPER_CACHE_DIR', 'Not set')}")

def main():
    models = ["tiny", "base", "small", "medium", "large"]
    print("Available models:", ", ".join(models))
    model_size = input("Enter model size (default: small): ").lower().strip()
    
    if not model_size:
        model_size = "small"
    elif model_size not in models:
        print(f"Invalid model size. Using 'small' instead.")
        model_size = "small"
    
    transcribe_with_model(model_size)

if __name__ == "__main__":
    main()