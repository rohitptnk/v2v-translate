import gradio as gr
from my_transcribe import transcribe_audio_locally
from my_translate import translate_text
from my_tts import text_to_speech

def voice_to_voice(audio):
    # Step 1: Transcribe
    result = transcribe_audio_locally(audio, model_size="base")
    source_text = result["text"]

    # Step 2: Translate
    translated = translate_text(source_text, from_lang="en", to_lang="hi")

    # Step 3: TTS
    output_audio_path = text_to_speech(translated, "v2/hi_speaker_2")

    return output_audio_path, source_text, translated

iface = gr.Interface(
    fn=voice_to_voice,
    inputs=gr.Audio(type="filepath", label="Upload English Audio"),
    outputs=[
        gr.Audio(label="Translated Audio (Hindi)"),
        gr.Textbox(label="Transcribed Text (English)"),
        gr.Textbox(label="Translated Text (Hindi)"),
    ],
    title="Voice-to-Voice Translator",
    description="Upload an English audio file. It will be transcribed, translated to Hindi, and synthesized as speech."
)

if __name__ == "__main__":
    iface.launch()
