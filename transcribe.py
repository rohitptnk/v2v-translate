def transcribe_audio_locally(audio_file_path, model_size="base"):
    """
    Transcribe audio using locally installed Whisper

    Args:
        audio_file_path (str): Path to audio file
        model_size (str): Whisper model size (tiny, base, small, medium, large)

    Returns:
        dict: Transcription result containing text and other info
    """
    import whisper

    # Load the model
    model = whisper.load_model(model_size)

    # Transcribe the audio
    result = model.transcribe(audio_file_path)

    return result