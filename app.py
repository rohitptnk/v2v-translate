from my_transcribe import transcribe_audio_locally
from my_translate import translate_text
from my_tts import text_to_speech

def voice_to_voice(audio_file_path):
    # Step 1: Transcribe
    result = transcribe_audio_locally(audio_file_path, model_size="base")
    source_text = result["text"]
    print("Transcribed:", source_text)

    # Step 2: Translate
    translated = translate_text(source_text, from_lang="en", to_lang="hi")
    print("Translated:", translated)

    # Step 3: Text to Speech
    output_audio_path = text_to_speech(translated, "v2/hi_speaker_2")
    print("Saved translated speech to:", output_audio_path)

    return output_audio_path

if __name__ == "__main__":
    voice_to_voice("Input Audio Sample.wav")
